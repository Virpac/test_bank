from typing import List,Any

import pytest
import logging

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.fixtures.user_fixture import *
from src.main.api.fixtures.db_fixture import *

@pytest.fixture
def created_obj() :
    objects : List[Any] = []
    yield objects
    clean_user(objects)

def clean_user(objects: List[Any]) :
    api_manager  = ApiManager(objects)
    for user in objects :
        if isinstance(user,CreateUserResponse):
            api_manager.admin_steps.delete_user(user.id)
        else :
            logging.warning(f"user {user.id} is not an instance of CreateUserResponse")


@pytest.fixture
def api_manager(created_obj):
    return ApiManager(created_obj)