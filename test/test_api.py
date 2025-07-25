import requests
import pytest
import allure
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject




def test_create_object(): #  класс для работы с созданием объектов
    new_object_endpoint = CreateObject()
    payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": 2019,
         "price": 1849.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
    new_object_endpoint.new_object(payload=payload) #  Отправляем запрос на создание объекта
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(payload) #  проверка что имя в ответе соответствует отправленному
    #response = requests.post(
     #   url='https://api.restful-api.dev/objects' ,json=payload
   # ).json() #описанно в классе
    #assert response['name'] == payload['name']
    #print(response) #описанно в классе


def test_get_object(obj_id): # Получаем ID объекта из фикстуры
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id) # запрос на получение объекта по ID
    get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_response_id(obj_id) # проверка что полученный объект содержит ожидаемые данные

    #print(obj_id)
    #response=requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
    #assert response['id'] == obj_id
    #print(response)


def test_update_object(obj_id):
    update_obj_endpoint = UpdateObject()
    payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": 3019,
         "price": 1849.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
    update_obj_endpoint.update_by_id(obj_id,payload)
    update_obj_endpoint.check_response_is_200()
    update_obj_endpoint.check_response_name(payload['name'])
    #response=requests.put(
    #    url=f'https://api.restful-api.dev/objects/{obj_id}',
     #   json=payload
    #).json()
    #assert  response['name'] == payload['name']
    #print(response)


def test_delete_object(obj_id): # Получаем ID объекта из фикстуры
    get_obj_endpoint = GetObject() #  пытаемся получить удаленный объект
    delete_obj_endpoint = DeleteObject() #  Инициализируем класс для работы с удалением объектов
    delete_obj_endpoint.delete_by_id(obj_id)  #   запрос на удаление объекта по ID
    delete_obj_endpoint.check_response_is_200() #  Проверяем  статус ответа 200 (OK)
    get_obj_endpoint.get_by_id(obj_id) #  пытаемся получить удаленный объект
    get_obj_endpoint.check_response_is_404() # объект действительно удален (статус 404)
    #response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    #assert response.status_code == 200
    #response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    #assert response.status_code == 404
    #print(response)

#запуск pytest -v -s
# запус с отчетом pytest -v -s --alluredir results