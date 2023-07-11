import requests

class ToDo:
    def __init__(self, url):
        self.url = url


# получение всего списка задач
    def get_list_todo(self, params_to_add=None):
        resp = requests.get(self.url, params=params_to_add)
        return resp.json()


# добавление новой задачи
    def add_new_task(self, title):
        body = {
            "title": title,
        }
        result = requests.post(self.url, json=body)
        return result.json()


# переменинование названия задачи
    def rename_task(self, id, new_name):
        name = {
            "title": new_name
        }
        result = requests.patch(self.url + str(id), json=name)
        return result.json()


# получение конкретной задачи из списка
    def get_one_task(self, id):
        result = requests.get(self.url + str(id))
        return result.json()


# oтметка задачи «Выполнена»
    def task_done(self, id, completed = True):
        body = {
            "completed": completed,
        }
        result = requests.patch(self.url + str(id), json=body)
        return result.json()


# cнятие отметки «Выполнена»
    def task_no_done(self, id, completed = False):
        body = {
            "completed": completed,
        }
        result = requests.patch(self.url + str(id), json=body)
        return result.json()


# удаление задачи
    def delete_task(self, id):
        result = requests.delete(self.url + str(id))
        return result.status_code