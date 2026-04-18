import requests

from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.requests.requester import Requester


class DepositAccountRequester(Requester):
    def post(self,deposit_account_request : DepositAccountRequest):
        url = f"{self.base_url}/account/deposit"
        response = requests.post(
            url=url,
            json = deposit_account_request.model_dump(),
            headers = self.headers
        )
        self.response_spec(response)
        return response
