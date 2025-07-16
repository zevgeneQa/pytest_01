import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

@pytest.fixture() # Фикстура создает тестовый объект перед тестом и удаляет его после
def obj_id():
    create_object = CreateObject()  #  класс создания объекта
    payload = { #Подготавливаем данные для создания объекта
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_object.new_object(payload) #  запрос на создание объекта
   # response = requests.post(
   #     url='https://api.restful-api.dev/objects', json=payload
   # ).json()
    yield create_object.response_json['id'] # возвращаем ID созданного объекта для использования в тестах
    delete_object = DeleteObject() #  После выполнения теста!!! удаляем созданный объект
    delete_object.delete_by_id(create_object.response_json['id'])
    #requests.delete(f'https://api.restful-api.dev/objects/{response["id"]}')


