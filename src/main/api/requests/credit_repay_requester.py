from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.requests.requester import Requester
import requests

class CreditRepayRequester(Requester):
    def post(self,credit_repay_request: CreditRepayRequest):
        url = f"{self.base_url}/credit/repay"
        response = requests.post(url, json=credit_repay_request.model_dump(),headers=self.headers)
        self.response_spec(response)
        return response