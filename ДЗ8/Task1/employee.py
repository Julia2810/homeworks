import requests
import json



class Employee:

    def __init__(self, url):
        self.url = url

    # получение авторизационного токена
    def get_token(self, user='bloom', password='fire-fairy'):
        body = {
            'username': user,
            'password': password
        }
        result = requests.post(self.url + 'auth/login', json=body)
        return result.json()["userToken"]

    # получение списка компаний
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()

    # получение списка сотрудников одной компании
    def get_list_employee(self, id):
        resp = requests.get(self.url + '/employee' + str(id))
        return resp.json()

    # добавление одного сотрудника
    def add_new_employee(self, id_company, first_name, last_name, middle_name, phone, url):
        body = {
            "companyId": id_company,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "phone": phone,
            "url": url
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        result = requests.post(self.url + 'employee', json=body, headers=my_headers)
        return result.json()

    # получить сотрудника по id
    def get_employee(self, id_employee):
        result = requests.get(self.url + 'employee' + str(id_employee))
        return result.json()


    #изменить информацию о сотруднике
    def edit_employee(self, id, new_last_name, new_email, new_url, is_active = True):
        body = {
                "lastName": new_last_name,
                "email": new_email,
                "url": new_url,
                "isActive": is_active
            }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        result = requests.patch(self.url + 'employee' + str(id), json=body, headers=my_headers)
        return result.json()

