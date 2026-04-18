import requests

from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_request_response import CreditRequestResponse
from src.main.api.requests.requester import Requester


class CreditRequestRequester(Requester):
    def post(self,credit_request : CreditRequest):
        url = f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            json = credit_request.model_dump(),
            headers= self.headers,
        )
        self.response_spec(response)
        return CreditRequestResponse(**response.json())