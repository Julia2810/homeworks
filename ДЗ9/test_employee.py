from sqlalchemy import create_engine
import psycopg2
from CompanyAPI import Employee
from CompanyTable import Table


api = Employee("https://x-clients-be.onrender.com")
db = Table("postgresql://x_clients_user:2hdwfMCel2i7SyZeOghoUVVOOwnpyfEL@dpg-chdkl0ak728nnn00sqv0-a.frankfurt-postgres.render.com/x_clients_db_yjdt")


# убедимся, что в базе есть компании, из которых можно получить список сотрудников
def test_get_company_list():
    companies_list_api = api.get_company_list()
    companies_list_db = db.get_companies()
    assert len(companies_list_api) == len(companies_list_db)
    
    
# получение списка сотрудников из одной компании
def test_list_employee():
    employee_list_api = api.get_list_employee(40)
    employee_list_db = db.get_list_employee(40)
    assert len(employee_list_api) == len(employee_list_db)
    
    
#добавление одного сотрудника
def test_add_one_employee():
    body_api = api.get_list_employee(40)
    len_before = len(body_api)
    
    id_company = 40
    first_name = 'Ivan'
    last_name = 'Petrov'
    middle_name = 'Ivanovich'
    phone = '+79575684587'
    url = 'https://i.pinimg.com/736x/29/20/f8/2920f8efeb542ba40f107f6d9cfd34e9.jpg'

    new_employee = api.add_new_employee(id_company, first_name, last_name, middle_name, phone, url)
    new_id = new_employee['id']

    body_api = api.get_list_employee(id_company)

    len_after = len(body_api)
    
    db.delete_employee(new_id)

    assert len_after - len_before == 1
    assert new_employee['id'] == new_id
            

#получение сотрудника по id
def test_get_employee():
    db.add_employee('Sergey', 'Ivanov', 'Petrovich', '+79954684585', 'https://avatars.mds.yandex.net/i?id=16cab1e80a8c3d417faf0d45eab6537a70a00021-8185177-images-thumbs&n=13', 40)

    max_id = db.get_max_id()
    new_employee = api.get_employee(max_id)

    assert new_employee['id'] == max_id
   


#изменение информации о сотруднике
def test_edit_employee():
    db.add_employee('Lev', 'Sidorov', 'Petrovich', '+75658456956', 'https://happypik.ru/wp-content/uploads/2019/09/njashnye-kotiki8.jpg', 40)

    max_id = db.get_max_id()

    id_new_employee = max_id

    new_last_name = 'Voronov'
    new_email = 'tester_1@email.com'
    new_url = 'https://klike.net/uploads/posts/2022-06/1654842544_1.jpg'
    is_active = True

    new_data_employee = api.edit_employee(id_new_employee, new_last_name, new_email, new_url, is_active)

    assert new_data_employee['email'] == new_email
    assert new_data_employee['url'] == new_url
    assert new_data_employee['isActive'] == is_active