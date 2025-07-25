import requests
from endpoints.base_endpoint import Endpoint

class GetObject(Endpoint):


    def get_by_id(self, id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{id}')
        self.response_json = self.response.json()# метод получения объекта по id
        return self.response_json

    def check_response_id(self, object_id):
        assert self.response_json['id'] == object_id#проверяет что ответ с правильным id


    def check_response_is_404(self):
        assert self.response.status_code == 404