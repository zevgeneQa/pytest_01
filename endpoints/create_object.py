import requests
from endpoints.base_endpoint import Endpoint


class CreateObject(Endpoint):


    def new_object(self,payload):
        self.response = requests.post(url='https://api.restful-api.dev/objects' ,json=payload)
        self.response_json = self.response.json()

    def check_name(self,name,payload):
        assert self.response_json['name'] == payload['name']

