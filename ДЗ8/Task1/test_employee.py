import requests
from employee import Employee

api = Employee("https://x-clients-be.onrender.com")

# убедимся, что в базе есть компании, из которых можно получить список сотрудников
def test_get_company_list():
    companies = api.get_company_list()
    assert len(companies) > 0


# получение списка сотрудников из одной компании
def test_list_employee():
    employees = api.get_list_employee(40)
    assert len(employees) > 0


#добавление одного сотрудника
def test_add_one_employee():
    body = api.get_list_employee(40)
    len_before = len(body)

    id_company = 40
    first_name = 'Ivan'
    last_name = 'Petrov'
    middle_name = 'Ivanovich'
    phone = '+79575684587'
    url = 'https://i.pinimg.com/736x/29/20/f8/2920f8efeb542ba40f107f6d9cfd34e9.jpg'

    new_employee = api.add_new_employee(id_company, first_name, last_name, middle_name, phone, url)
    new_id = new_employee['id']

    body = api.get_list_employee(id_company)

    len_after = len(body)

    assert len_after - len_before == 0
    assert new_employee['id'] == new_id


#получение сотрудника по id
def test_get_employee():
    id_company = 40
    first_name = 'Sergey'
    last_name = 'Ivanov'
    middle_name = 'Petrovich'
    phone = '+79954684585'
    url = 'https://avatars.mds.yandex.net/i?id=16cab1e80a8c3d417faf0d45eab6537a70a00021-8185177-images-thumbs&n=13'
    new_employee = api.add_new_employee(id_company, first_name, last_name, middle_name, phone, url)

    id_new_employee = new_employee['id']

    one_employee = api.get_employee(id_new_employee)

    assert one_employee['companyId'] == id_company
    assert one_employee['id'] == id_new_employee
    assert one_employee['firstName'] == first_name
    assert one_employee['lastName'] == last_name
    assert one_employee['middleName'] == middle_name


#изменение информации о сотруднике
def test_edit_employee():
    id_company = 40
    first_name = 'Lev'
    last_name = 'Sidorov'
    middle_name = 'Sergeevich'
    phone = '+75658456956'
    url = 'https://happypik.ru/wp-content/uploads/2019/09/njashnye-kotiki8.jpg'

    new_employee = api.add_new_employee(id_company, first_name, last_name, middle_name, phone, url)

    id_new_employee = new_employee['id']

    new_last_name = 'Voronov'
    new_email = 'tester_1@email.com'
    new_url = 'https://klike.net/uploads/posts/2022-06/1654842544_1.jpg'
    is_active = True

    new_data_employee = api.edit_employee(id_new_employee, new_last_name, new_email, new_url, is_active)

    assert new_data_employee['email'] == new_email
    assert new_data_employee['url'] == new_url
    assert new_data_employee['isActive'] == is_active