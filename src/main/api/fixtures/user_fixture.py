import pytest

from src.main.api.models.create_user_requests import CreateUserRequest,CreateUserCreditRequest
from src.main.api.generators.model_generator import RandomModelGenerator

@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_user_credit_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request