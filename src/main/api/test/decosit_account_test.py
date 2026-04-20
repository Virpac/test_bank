from sqlalchemy.orm import Session

from src.main.api.models.create_user_requests import CreateUserRequest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.db.crud.account_crud import AccountCrudDb as Account
import pytest

class TestDepositAccount():
    @pytest.mark.parametrize(
        "amount",
        [
            1000,9000
        ]
    )
    def test_deposit_account_valid(self,api_manager: ApiManager,create_account_request,amount: float,db_session: Session):
        deposit_account_request = DepositAccountRequest(accountId=create_account_request["account"].id,amount=amount)
        response = api_manager.user_steps.deposit_account_valid(create_account_request["user"],deposit_account_request)
        assert response.balance == deposit_account_request.amount
        account_from_db = Account.get_account_by_id(db_session, response.id)
        assert account_from_db.balance == amount , 'Баланс в бд не обновился'

    @pytest.mark.parametrize(
        "amount",
        [
            999,9001
        ]
    )
    def test_deposit_account_invalid(self,api_manager: ApiManager,create_account_request,amount: float,db_session: Session):
        deposit_account_request = DepositAccountRequest(accountId=create_account_request["account"].id,amount=amount)
        response = api_manager.user_steps.deposit_account_valid(create_account_request["user"],deposit_account_request)
        account_from_db = Account.get_account_by_id(db_session, create_account_request.id)
        assert account_from_db.balance is not amount , 'Аккаунт пополнился'





        
