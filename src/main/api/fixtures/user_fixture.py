import pytest

from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
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

@pytest.fixture
def create_account_request(api_manager,create_user_request):
    response = api_manager.user_steps.create_account(create_user_request)
    return {
        "account": response,
        "user": create_user_request
    }

@pytest.fixture
def create_account_credit_request(api_manager,create_user_credit_request):
    response = api_manager.user_steps.create_account(create_user_credit_request)
    return {
        "account": response,
        "user": create_user_credit_request
    }

@pytest.fixture
def deposit_request(api_manager,create_user_request,amount):
    from_response = api_manager.user_steps.create_account(create_user_request)
    deposit_account_request = DepositAccountRequest(accountId=from_response.id, amount=amount)
    api_manager.user_steps.deposit_account_valid(create_user_request, deposit_account_request)
    to_response = api_manager.user_steps.create_account(create_user_request)
    return {
        "from_response": from_response,
        "to_response": to_response,
        "user": create_user_request
    }

@pytest.fixture
def deposit_invalid_request(api_manager,create_user_request):
    from_response = api_manager.user_steps.create_account(create_user_request)
    deposit_account_request = DepositAccountRequest(accountId=from_response.id, amount=9000)
    api_manager.user_steps.deposit_account_valid(create_user_request, deposit_account_request)
    api_manager.user_steps.deposit_account_valid(create_user_request, deposit_account_request)
    to_response = api_manager.user_steps.create_account(create_user_request)
    return {
        "from_response": from_response,
        "to_response": to_response,
        "user": create_user_request
    }

@pytest.fixture
def create_credit_request(api_manager,create_account_credit_request,amount):
    credit_request = CreditRequest(accountId=create_account_credit_request["account"].id, amount=amount, termMonths=12)
    credit_response = api_manager.user_steps.credit_request(create_account_credit_request["user"], credit_request)
    deposit_account_request = DepositAccountRequest(accountId=create_account_credit_request["account"].id, amount=amount)
    api_manager.user_steps.deposit_account_valid(create_account_credit_request["user"], deposit_account_request)
    return {
        "credit_response": credit_response,
        "user" : create_account_credit_request["user"]
    }