import pytest


def pytest_collection_modifyitems(config, items):
    for item in items:
        path = str(item.fspath)
        if "open_webui/test/apps/webui/routers/" in path:
            item.add_marker(pytest.mark.integration)
        elif "open_webui/test/apps/webui/storage/" in path:
            item.add_marker(pytest.mark.integration)
            item.add_marker(pytest.mark.slow)
        elif "open_webui/test/util/" in path:
            item.add_marker(pytest.mark.fast)
        else:
            item.add_marker(pytest.mark.fast)
