import requests

def test_login_api_dev():
    payload = {"email" : "user@example.com","password" : "password"}
    response=requests.post(url='https://ulcamp-backend-develop.k8s.zetest.site/api/login', json=payload).json()
    print(response)