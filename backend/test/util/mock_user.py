"""Dependency override helper for authenticated FastAPI routes in tests."""

from __future__ import annotations

from contextlib import contextmanager
from types import SimpleNamespace
from typing import Iterator

from open_webui.main import app
from open_webui.utils.auth import get_admin_user, get_current_user, get_verified_user


@contextmanager
def mock_webui_user(
    id: str = "1",
    name: str = "John Doe",
    email: str = "john.doe@openwebui.com",
    role: str = "user",
    profile_image_url: str = "/user.png",
) -> Iterator[SimpleNamespace]:
    user = SimpleNamespace(
        id=id,
        name=name,
        email=email,
        role=role,
        profile_image_url=profile_image_url,
        bio=None,
        gender=None,
        date_of_birth=None,
        status_emoji=None,
        status_message=None,
        status_expires_at=None,
    )

    previous_overrides = app.dependency_overrides.copy()
    app.dependency_overrides[get_current_user] = lambda: user
    app.dependency_overrides[get_verified_user] = lambda: user
    app.dependency_overrides[get_admin_user] = lambda: user

    try:
        yield user
    finally:
        app.dependency_overrides = previous_overrides
