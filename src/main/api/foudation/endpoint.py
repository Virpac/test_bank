from enum import Enum

from src.main.api.models.base_model import BaseModel
from typing import Optional,Type
from dataclasses import dataclass
from src.main.api.models.create_user_requests import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_request_response import CreditRequestResponse
from src.main.api.models.login_user_requests import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.deposit_account_response import DepositAccountResponse
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.transfer_account_response import TransferAccountResponse


@dataclass(frozen=True)
class EndpointConfiguration:
    url : str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model = CreateUserRequest,
        url = "/admin/create",
        response_model = CreateUserResponse
    )
    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model = None,
        url = "/admin/users",
        response_model = None
    )
    LOGIN_USER = EndpointConfiguration(
        request_model = LoginUserRequest,
        url = "/auth/token/login",
        response_model = LoginUserResponse
    )

    CREATE_ACCOUNT = EndpointConfiguration(
        request_model= None,
        url = "/account/create",
        response_model = CreateAccountResponse
    )

    DEPOSIT_ACCOUNT = EndpointConfiguration(
        request_model= DepositAccountRequest,
        url = "/account/deposit",
        response_model= DepositAccountResponse
    )

    CREDIT_REQUEST = EndpointConfiguration(
        request_model= CreditRequest,
        url = "/credit/request",
        response_model= CreditRequestResponse
    )

    CREDIT_REPAY = EndpointConfiguration(
        request_model = CreditRepayRequest,
        url = "/credit/repay",
        response_model = CreditRepayResponse
    )

    TRANSFER_ACCOUNT = EndpointConfiguration(
        request_model= TransferAccountRequest,
        url = "/account/transfer",
        response_model= TransferAccountResponse
    )

