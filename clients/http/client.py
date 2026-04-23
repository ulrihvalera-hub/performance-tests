client.py
from httpx import Client

class HTTPClient:
    def __init__(self, client: Client):
        self.client = client

    def get (self, url= URL | str, params= QueryParams | None = None) -> Response:
        return selfr.client.get(url,params=params)


    def post(self,url= str,json: Any | None=None) -> Response:
        return self.client.post(url=url, json=json)
clients.py