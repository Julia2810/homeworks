import requests

from todo import ToDo

url_api = ToDo('https://todo-app-sky.herokuapp.com/')


# получение всего списка задач
def test_get_list_to_do():
    result = url_api.get_list_todo()

    assert len(result)>0


# создание новой задачи
def test_add_new_task():
    res1 = url_api.get_list_todo()
    result = url_api.add_new_task('Задачка')
    res2 = url_api.get_list_todo()

    assert len(res2)-len(res1) == 1
    assert result['title'] == 'Задачка'


# изменение названия задачи
def test_rename_task():
    name1 = url_api.add_new_task('Задачка 1')
    new_id = name1['id']
    new_name = 'Задачка 2'
    name2 = url_api.rename_task(new_id, new_name)

    assert name2['title'] == 'Задачка 2'
    assert name2['id'] == new_id


# получение одной задачи из списка
def test_get_one_task():
    new_task = url_api.add_new_task('Новая задача')
    new_id = new_task['id']
    result = url_api.get_one_task(new_id)

    assert result['title'] == 'Новая задача'
    assert result['id'] == new_id


# отметка "Выполнена"
def test_task_done():
    new_task = url_api.add_new_task('Фиксики')
    new_id = new_task['id']
    result = url_api.task_done(new_id)

    assert result["completed"] == True


# снятие отметки "Выполнена"
def test_task_no_done():
    new_task = url_api.add_new_task('Лунтик')
    new_id = new_task['id']
    result1 = url_api.task_done(new_id)
    result2 = url_api.task_no_done(new_id)


    assert result1["completed"] == True
    assert result2["completed"] == False

# удаление задачи
def test_delete_task():
    new_task = url_api.add_new_task('Смешарики')
    new_id = new_task['id']
    result = url_api.delete_task(new_id)

    assert result['id'] == new_id
    assert result['title'] == 'Смешарики'

    all_list = url_api.get_list_todo()

    assert all_list[-1]['id'] != new_id