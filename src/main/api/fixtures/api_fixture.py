import pytest


from src.main.api.classes.api_manager import ApiManager


@pytest.fixture
def api_mager(created_obj):
    return ApiManager(created_obj)