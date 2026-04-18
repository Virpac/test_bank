import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.db.crud.account_crud import AccountCrudDb as Account


class TestTransferAccount():
    @pytest.mark.parametrize(
        "amount",
        [1000,9000]
    )
    def test_transfer_account(self,api_manager:ApiManager, create_user_request, db_session: Session, amount: float):
        from_response = api_manager.user_steps.create_account(create_user_request)
        deposit_account_request = DepositAccountRequest(accountId=from_response.id, amount=amount)
        api_manager.user_steps.deposit_account_valid(create_user_request, deposit_account_request)

        to_response = api_manager.user_steps.create_account(create_user_request)
        transfer_account_request = TransferAccountRequest(fromAccountId=from_response.id,toAccountId=to_response.id, amount=amount)
        response = api_manager.user_steps.transfer(create_user_request,transfer_account_request)
        assert response.fromAccountId == transfer_account_request.fromAccountId
        account_from_db = Account.get_account_by_id(db_session, to_response.id)
        assert account_from_db.balance == amount , 'Баланс не обновился'
    @pytest.mark.parametrize(
        "amount",
        [490,10001,-1]
    )
    def test_transfer_account_invalid(self,api_manager:ApiManager, create_user_request, db_session: Session, amount: float):
        from_response = api_manager.user_steps.create_account(create_user_request)
        deposit_account_request = DepositAccountRequest(accountId=from_response.id, amount=9000)
        api_manager.user_steps.deposit_account_valid(create_user_request, deposit_account_request)
        api_manager.user_steps.deposit_account_valid(create_user_request, deposit_account_request)

        to_response = api_manager.user_steps.create_account(create_user_request)
        transfer_account_request = TransferAccountRequest(fromAccountId=from_response.id,toAccountId=to_response.id, amount=amount)
        api_manager.user_steps.transfer_invalid(create_user_request,transfer_account_request)
        account_from_db = Account.get_account_by_id(db_session, to_response.id)
        assert account_from_db.balance is not amount, 'Баланс ошибчно  пополнился'


