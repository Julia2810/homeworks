from sqlalchemy import create_engine
import allure
import psycopg2
from EmployeeAPI import Employee
from EmployeeSQL import Table


api = Employee("https://x-clients-be.onrender.com")
db = Table("postgresql://x_clients_user:2hdwfMCel2i7SyZeOghoUVVOOwnpyfEL@dpg-chdkl0ak728nnn00sqv0-a.frankfurt-postgres.render.com/x_clients_db_yjdt")


# убедимся, что в базе есть компании, из которых можно получить список сотрудников
@allure.title("Получение списка компаний")
@allure.description("Запросы списка компаний через api и БД и их сравнение")
@allure.feature("READ")
@allure.severity("TRIVIAL")
def test_get_company_list():
    """
    Тест на сравнение длины списка компаний, полученного через API и запроса к БД
    """
    with allure.step("Получить список компаний через API"):
        companies_list_api = api.get_company_list()

    with allure.step("Получить список компаний через БД"):
        companies_list_db = db.get_companies()

    with allure.step("Проверить, что полученные списки компаний равны"):
        assert len(companies_list_api) == len(companies_list_db)
    
    
# получение списка сотрудников из одной компании
@allure.title("Получение списка сотрудников")
@allure.description("Запросы списка сотрудников компании через api и БД и их сравнение")
@allure.feature("READ")
@allure.severity("TRIVIAL")
def test_list_employee():
    """
    Тест на сравнение длины списка сотрудников, полученного через API и запроса к БД
    """
    with allure.step("Получить список сотрудников через API"):
        employee_list_api = api.get_list_employee(40)

    with allure.step("Получить список сотрудников через БД"):
        employee_list_db = db.get_list_employee(40)

    with allure.step("Проверить, что полученные списки сотрудников равны"):
        assert len(employee_list_api) == len(employee_list_db)
    
    
#добавление одного сотрудника
@allure.title("Создание нового сотрудника")
@allure.description("Создание нового сотрудника компании и удаление из БД")
@allure.feature("CREATE")
@allure.severity("MAJOR")
def test_add_one_employee():
    """
    Тест на создание нового сотрудника, проверка длины списка сотрудников до добавления нового и после
    """
    with allure.step("Получить список сотрудников через API"):
        body_api = api.get_list_employee(40)

    with allure.step("Определить длину списка сотрудников до добавления нового"):
        len_before = len(body_api)

    with allure.step("Создать нового сотрудника"):
        id_company = 40
        first_name = 'Ivan'
        last_name = 'Petrov'
        middle_name = 'Ivanovich'
        phone = '+79575684587'
        url = 'https://i.pinimg.com/736x/29/20/f8/2920f8efeb542ba40f107f6d9cfd34e9.jpg'
        new_employee = api.add_new_employee(id_company, first_name, last_name, middle_name, phone, url)
        new_id = new_employee['id']

    with allure.step("Получаем список сотрудников после добавления нового"):
        body_api = api.get_list_employee(id_company)

    with allure.step("Определяем длину списка после добавления нового"):
        len_after = len(body_api)

    with allure.step("Удаляем нового сотрудника через запрос к БД"):
        db.delete_employee(new_id)

    with allure.step("Проверяем разницу между длиной до и после добавления нового сотрудника"):
        assert len_after - len_before == 1
        assert new_employee['id'] == new_id
            

#получение сотрудника по id
@allure.title("Получение данных о сотруднике")
@allure.description("Запрос id сотрудника")
@allure.feature("READ")
@allure.severity("TRIVIAL")
def test_get_employee():
    """
    Тест на получение информации о сотруднике по id 
    """
    with allure.step("Создать нового сотрудника через запрос к БД"):
        db.add_employee('Sergey', 'Ivanov', 'Petrovich', '+79954684585', 'https://avatars.mds.yandex.net/i?id=16cab1e80a8c3d417faf0d45eab6537a70a00021-8185177-images-thumbs&n=13', 40)
        max_id = db.get_max_id()

    with allure.step("Получаем информацию по новому сотруднику через API"):
        new_employee = api.get_employee(max_id)

    with allure.step("Проверяем, что id нового сотрудника, созданного через БД равен id, полученому через API"):
        assert new_employee['id'] == max_id
   


#изменение информации о сотруднике
@allure.title("Изменение данных о сотруднике")
@allure.description("Проверка возможности изменения данных о сотруднике")
@allure.feature("CREATE")
@allure.severity("MAJOR")
def test_edit_employee():
    """
    Тест на изменение данных сотрудника
    """
    with allure.step("Создать нового сотрудника через запрос к БД"):
        db.add_employee('Lev', 'Sidorov', 'Petrovich', '+75658456956', 'https://happypik.ru/wp-content/uploads/2019/09/njashnye-kotiki8.jpg', 40)
        max_id = db.get_max_id()

    with allure.step("Вносим изменения к созданному сотруднику через API"):
        id_new_employee = max_id
        new_last_name = 'Voronov'
        new_email = 'tester_1@email.com'
        new_url = 'https://klike.net/uploads/posts/2022-06/1654842544_1.jpg'
        is_active = True

    with allure.step("Отправляем запрос на изменение данных о сотруднике через API"):
        new_data_employee = api.edit_employee(id_new_employee, new_last_name, new_email, new_url, is_active)

    with allure.step("Проверяем, что информация о сотруднике изменилась"):
        assert new_data_employee['email'] == new_email
        assert new_data_employee['url'] == new_url
        assert new_data_employee['isActive'] == is_active