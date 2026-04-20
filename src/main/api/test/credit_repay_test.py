import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit


class TestCreditRepay:
    @pytest.mark.parametrize(
        "amount",
        [
            5000,9000
        ]
    )
    def test_credit_repay(self,api_manager: ApiManager, create_credit_request, amount: float, db_session: Session):
        credit_repay_request = CreditRepayRequest(creditId=create_credit_request["credit_response"].creditId,accountId=create_credit_request["credit_response"].id,amount=amount)
        repay_response = api_manager.user_steps.credit_repay(create_credit_request["user"],credit_repay_request)
        assert repay_response.amountDeposited == credit_repay_request.amount
        credit_from_db = Credit.get_credit_id(db_session,create_credit_request["credit_response"].id)
        assert credit_from_db.balance == 0