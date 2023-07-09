import requests
import json

from employee import Employee

api = Employee("https://x-clients-be.onrender.com")

# убедимся, что в базе есть компании, из которых можно получить список сотрудников
def test_get_company_list():
    companies = api.get_company_list()
    assert len(companies) > 0

# получение списка сотрудников из одной компании
def test_list_employee():
    employees = api.get_list_employee(36)
    assert len(employees) > 0

#добавление одного сотрудника
def test_add_one_employee():
    body = api.get_list_employee(36)
    len_before = len(body)

    id_company = 36
    first_name = 'Ivan'
    last_name = 'Petrov'
    middle_name = 'Ivanovich'
    phone = '+79575684587'
    url = 'test@email.com'

    new_employee = api.add_new_employee(id_company, first_name, last_name, middle_name, phone, url)

    new_id = new_employee['id']

    body = api.get_list_employee(36)

    len_after = len(body)

    assert len_after - len_before == 1
    assert new_employee['id'] == new_id



#получение сотрудника по id
def test_get_employee():
    id_company = 35
    first_name = 'Sergey'
    last_name = 'Ivanov'
    middle_name = 'Petrovich'
    phone = '+79954684585'
    url = 'test_test@email.com'
    new_employee = api.add_new_employee(id_company, first_name, last_name, middle_name, phone, url)

    id_new_employee = new_employee['id']

    one_employee = api.get_employee(id_new_employee)

    assert one_employee['companyId'] == id_company
    assert one_employee['id'] == id_new_employee
    assert one_employee['firstName'] == first_name
    assert one_employee['lastName'] == last_name
    assert one_employee['middleName'] == middle_name
    assert one_employee['url'] == url

#изменение информации о сотруднике
def test_edit_employee():
    id_company = 34
    first_name = 'Lev'
    last_name = 'Sidorov'
    middle_name = 'Sergeevich'
    phone = '+75658456956'
    url = 'test-test@email.com'

    new_employee = api.add_new_employee(id_company, first_name, last_name, middle_name, phone, url)

    id_new_employee = new_employee['id']

    new_last_name = 'Voronov'
    new_email = tester@email.com
    new_url = tester_qa@email.com
    is_active = True

    new_data_employee = api.edit_employee(id_new_employee, new_last_name, new_email, new_url, is_active)


    assert new_data_employee['lastName'] == new_last_name
    assert new_data_employee['email'] == new_email
    assert new_data_employee['url'] == new_url
    assert new_data_employee['isActive'] == is_active