import requests
import allure



class Employee:

    def __init__(self, url: str):
        self.url = url


    # получение авторизационного токена
    @allure.step("API.Получить токен для авторизации по логину и паролю = {user}:{password}")
    def get_token(self, user: str = 'bloom', password: str = 'fire-fairy') -> str:
        body = {
            'username': user,
            'password': password
        }
        result = requests.post(self.url + '/auth/login', json=body)
        return result.json()["userToken"]


    # получение списка компаний
    @allure.step("API.Получить список компаний")
    def get_company_list(self, params_to_add=None) -> dict:
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()
    
    # получение списка сотрудников одной компании
    @allure.step("API.Получить список компаний по id компании = {id}")
    def get_list_employee(self, id: int) -> dict:
        resp = requests.get(self.url + '/employee' + '?company=' + str(id))
        return resp.json()

    # добавление нового сотрудника
    @allure.step("API.Создание нового сотрудника по id компании = {id_company}")
    def add_new_employee(self, id_company: int, first_name: str, last_name: str, middle_name: str, phone: str, url: str) -> dict:
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
        result = requests.post(self.url + '/employee' + '?company=' + str(id_company), json=body, headers=my_headers)
        return result.json()


    # получить сотрудника по id
    @allure.step("API.Получение данных о сотруднике по его id = {id}")
    def get_employee(self, id_employee: int) -> dict:
        result = requests.get(self.url + '/employee/' + str(id_employee))
        return result.json()


    #изменить информацию о сотруднике
    @allure.step("API.Изменить информацию о сотруднике по его id = {id}")
    def edit_employee(self, id: int, new_last_name: str, new_email: str, new_url: str, is_active = True) -> dict:
        body = {
                "lastName": new_last_name,
                "email": new_email,
                "url": new_url,
                "isActive": is_active
            }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        result = requests.patch(self.url + '/employee/' + str(id), json=body, headers=my_headers)
        return result.json()