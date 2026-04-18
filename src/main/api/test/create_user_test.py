import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.db_fixture import db_session
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_requests import CreateUserRequest
from src.main.api.db.crud.user_crud import UserCrudDB as User


@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_request",[(RandomModelGenerator.generate(CreateUserRequest))]
    )
    def test_create_user_valid(self , api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        user_from_db = User.get_user_by_username(db_session,create_user_request.username)
        assert user_from_db.username == create_user_request.username ,"Пользователя нет в бд"
        
    @pytest.mark.parametrize(
            "username,password",
        [
                ("абв","Pas!sw0rd"),
                ("ab","Pas!sw0rd"),
                ("abv!","Pas!sw0rd"),
                ("Max221","Pas!sw0rд"),
                ("Max222","pas!sw0rd"),
                ("Max223","Passw0rd"),
                ("Max224","Passwrd"),
                ("Max225","PASSWRD"),
                ("Max226","PASSWR!D"),

            ]
    )
    def test_create_invalid_user(self,db_session: Session,username: str,password: str,api_manager: ApiManager):

        create_user_request = CreateUserRequest(username=username,password=password,role="ROLE_USER")

        api_manager.admin_steps.create_invalid_user(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db is None , "Пользователь создан , ошибка"
