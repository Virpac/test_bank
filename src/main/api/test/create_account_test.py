import pytest

from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb as Account

@pytest.mark.api
class TestCreateAccount:
    def test_create_account(self,api_manager:ApiManager, create_user_request, db_session:Session):
        response = api_manager.user_steps.create_account(create_user_request)
        assert response.balance == 0
        account_from_db = Account.get_account_by_id(db_session,response.id)
        assert account_from_db.id == response.id , 'Аккаунт не создан id аккаунта нет в базе'
        assert account_from_db.balance is not None , 'Поле баланса отсутвует для созданного пользователя нет в бд'