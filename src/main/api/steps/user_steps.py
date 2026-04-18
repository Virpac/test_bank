from src.main.api.foudation.endpoint import Endpoint
from src.main.api.foudation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_requests import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.specs.request_specs import RequestsSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.foudation.requesters.requester import CrudRequester

class UserSteps(BaseSteps):
    def create_account(self,create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username,password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_create()
        ).post()
        return response

    def deposit_account_valid(self,create_user_request: CreateUserRequest, deposit_account_request: DepositAccountRequest):
        deposit_response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_account_request)
        return deposit_response

    def deposit_account_invalid(self,create_user_request: CreateUserRequest, deposit_account_request: DepositAccountRequest):
        deposit_response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(deposit_account_request)
        return deposit_response

    def credit_request(self,create_user_request: CreateUserRequest, credit_request: CreditRequest):
        credit_response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_create()
        ).post(credit_request)
        return credit_response

    def credit_request_invalid(self,create_user_request: CreateUserRequest, credit_request: CreditRequest):
        credit_response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_bad()
        ).post(credit_request)
        return credit_response

    def transfer(self,create_user_request: CreateUserRequest, transfer_account_request: TransferAccountRequest):
        transfer_response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(transfer_account_request)
        return transfer_response

    def transfer_invalid(self,create_user_request: CreateUserRequest, transfer_account_request: TransferAccountRequest):
        transfer_response = CrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(transfer_account_request)
        return transfer_response

    def credit_repay(self,create_user_request: CreateUserRequest, credit_repay_request: CreditRepayRequest):
        repay_response = ValidateCrudRequester(
            RequestsSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_ok()
        ).post(credit_repay_request)
        return repay_response