"""Test scaffolding for legacy router integration tests."""

from __future__ import annotations

import importlib
import os
import pkgutil
import tempfile
from contextlib import asynccontextmanager
from typing import Any
from urllib.parse import urlencode

# Keep tests isolated from local development databases.
_TEST_DATA_DIR = tempfile.mkdtemp(prefix="local-ai-hub-test-")
os.environ.setdefault("ENABLE_DB_MIGRATIONS", "False")
os.environ.setdefault("WEBUI_SECRET_KEY", "local-ai-hub-test-secret")
os.environ.setdefault("DATA_DIR", _TEST_DATA_DIR)
os.environ.setdefault("DATABASE_URL", f"sqlite:///{_TEST_DATA_DIR}/webui-test.db")

from fastapi.testclient import TestClient

from open_webui.internal.db import Base, engine
from open_webui.main import app
import open_webui.models as models_package


@asynccontextmanager
async def _noop_lifespan(_app):
    # Skip application startup side effects for fast and deterministic tests.
    yield


def _import_model_modules() -> None:
    for module_info in pkgutil.iter_modules(models_package.__path__):
        if module_info.ispkg:
            continue
        importlib.import_module(f"{models_package.__name__}.{module_info.name}")


class AbstractPostgresTest:
    BASE_PATH = ""
    fast_api_client: TestClient

    @classmethod
    def setup_class(cls) -> None:
        app.router.lifespan_context = _noop_lifespan
        _import_model_modules()
        Base.metadata.create_all(bind=engine)

        cls.fast_api_client = TestClient(app)
        cls.fast_api_client.headers.update({"Authorization": "Bearer integration-test-token"})
        cls._reset_database()

    @classmethod
    def teardown_class(cls) -> None:
        if hasattr(cls, "fast_api_client"):
            cls.fast_api_client.close()
        app.dependency_overrides.clear()
        cls._reset_database()

    def setup_method(self) -> None:
        app.dependency_overrides.clear()
        self._reset_database()

    def teardown_method(self) -> None:
        app.dependency_overrides.clear()

    @classmethod
    def _reset_database(cls) -> None:
        with engine.begin() as connection:
            for table in reversed(Base.metadata.sorted_tables):
                connection.execute(table.delete())

    @classmethod
    def create_url(cls, path: str = "", query_params: dict[str, Any] | None = None) -> str:
        normalized_path = path or ""
        if normalized_path and not normalized_path.startswith("/"):
            normalized_path = f"/{normalized_path}"

        url = f"{cls.BASE_PATH}{normalized_path}"
        if query_params:
            return f"{url}?{urlencode(query_params)}"
        return url
