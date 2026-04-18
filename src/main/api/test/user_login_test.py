import pytest
from src.main.api.requests.login_user_requester import LoginUserRequest


@pytest.mark.api
class TestUserLogin:
    def test_login_admin(self,api_manager):

        login_user_requests = LoginUserRequest(username="admin",password="123456")
        response = api_manager.admin_steps.login_user(login_user_requests)

        assert login_user_requests.username == response.user.username
        assert response.user.role == "ROLE_ADMIN"
    
    def test_login_user(self,api_manager,create_user_request):

        response = api_manager.admin_steps.login_user(create_user_request)


        assert create_user_request.username == response.user.username
        assert response.user.role == "ROLE_USER"
    

