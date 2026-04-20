import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.db.crud.account_crud import AccountCrudDb as Account


class TestTransferAccount():
    @pytest.mark.parametrize(
        "amount",
        [1000,9000]
    )
    def test_transfer_account(self,api_manager:ApiManager, deposit_request, db_session: Session, amount: float):
        transfer_account_request = TransferAccountRequest(fromAccountId=deposit_request["from_response"].id,toAccountId=deposit_request["to_response"].id, amount=amount)
        response = api_manager.user_steps.transfer(deposit_request["user"],transfer_account_request)
        assert response.fromAccountId == transfer_account_request.fromAccountId
        account_from_db = Account.get_account_by_id(db_session, deposit_request["to_response"].id)
        assert account_from_db.balance == amount , 'Баланс не обновился'

    @pytest.mark.parametrize(
        "amount",
        [490,10001,-1]
    )
    def test_transfer_account_invalid(self,api_manager:ApiManager, deposit_invalid_request, db_session: Session, amount: float):
        transfer_account_request = TransferAccountRequest(fromAccountId=deposit_invalid_request["from_response"].id,toAccountId=deposit_invalid_request["to_response"].id, amount=amount)
        response = api_manager.user_steps.transfer_invalid(deposit_invalid_request["user"],transfer_account_request)
        account_from_db = Account.get_account_by_id(db_session, deposit_invalid_request["to_response"].id)
        assert account_from_db.balance is not amount, 'Баланс ошибчно  пополнился'


