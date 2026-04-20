from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.credit_request import CreditRequest
import pytest
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit

class TestCreditRequest:
    @pytest.mark.parametrize(
        "amount",
        [
            5001.0,14999.0
        ]
    )
    def test_credit_request(self,api_manager: ApiManager, create_account_credit_request, amount: float, db_session: Session):
        credit_request = CreditRequest(accountId=create_account_credit_request["account"].id,amount=amount,termMonths=12)
        response = api_manager.user_steps.credit_request(create_account_credit_request["user"],credit_request)
        assert response.balance == credit_request.amount
        credit_from_db = Credit.get_credit_id(db_session,response.id)
        assert credit_from_db.balance == -amount , 'Кредит не равен балансу на который оформлялся'

    @pytest.mark.parametrize(
        "amount",[
            4999.0,15001.0
        ]
    )
    def test_credit_request_invalid(self,api_manager: ApiManager,create_account_credit_request,amount: float,db_session: Session):
        credit_request = CreditRequest(accountId=create_account_credit_request["account"].id,amount=amount,termMonths=12)
        response = api_manager.user_steps.credit_request_invalid(create_account_credit_request["user"],credit_request)
        credit_from_db = Credit.get_credit_id(db_session, create_account_credit_request["account"].id)
        assert credit_from_db is None, 'Кредит не равен балансу на который оформлялся'

