from sqlalchemy import create_engine
import allure
import psycopg2
from sqlalchemy.sql import text




class Table:
    
    def __init__(self, connection_string):
        """
        Иницилизируем класс Table

        Args:
            connection_string (str): Строка подключения к БД
        """
        self.db = create_engine(connection_string)

# получение списка компаний
    @allure.step("БД.Запросить список организаций")
    def get_companies(self) -> list:
        """
        Получение списка компаний через БД.

        Returns:
            list:  список сотрудников
        """
        sql = text("select * from company")
        with self.db.engine.connect() as conn:
            result = conn.execute(sql).fetchall()
        return result
    
    
# получение списка сотрудников одной компании
    @allure.step("БД.Запросить список сотрудников по id компании = {id}")
    def get_list_employee(self, id: int) -> list:
        """
        Получение списка сотрудников через БД.

        Args:
            id (int): id компании

        Returns:
            list: список все сотрудников компании
        """
        sql = text('select * from employee where "companyId" =:id')
        with self.db.engine.connect() as conn:
            result = conn.execute(sql, {'id': id}).fetchall()
        return result
    
    
# добавление одного сотрудника
    @allure.step("БД.Запрос на создание нового сотрудника")
    def add_employee(self, first_name: str, last_name: str, middle_name: str, phone: str, url: str, id: int) -> bool:
        """
        Добавление нового сотрудника.

        Args:
            first_name (str): имя нового сотрудника
            last_name (str): фамилия нового сотрудника
            middle_name (str): отчество нового сотрудника
            phone (str): телефон нового сотрудника
            url (str): адрес фото нового сотрудника
            id (int): id компании

        Returns:
            bool: True
        """
        sql = text('insert into employee ("first_name", "last_name", "middle_name", "phone", "avatar_url", "companyId") values (:new_first_name, :new_last_name, :new_middle_name, :new_phone, :new_avatar_url, :company_id)')
        with self.db.engine.connect() as conn:
            conn.execute(sql, {'new_first_name': first_name, 'new_last_name': last_name, 'new_middle_name': middle_name, 'new_phone': phone, 'new_avatar_url': url, 'company_id': id})
            conn.commit()
        return True
    
    
# удаление одного сотрудника по id
    @allure.step("БД.Запрос на удаление сотрудника по его id = {id}")
    def delete_employee(self, id: int) -> bool:
        """
        Удаление сотрудника.

        Args:
            id (int): id сотрудника

        Returns:
            bool: True 
        """
        sql = text('delete from employee where "id" =:employee_id')
        with self.db.engine.connect() as conn:
            conn.execute(sql, {'employee_id': id})
            conn.commit()
        return True
    
    
# получение id вновь созданного сотрудника
    @allure.step("БД.Запросить id сотрудника, добавленного последним")
    def get_max_id(self) -> int:
        """
        Получение id сотрудника, добавленного последним.

        Returns:
            int: id сотрудника
        """
        sql = text('select MAX("id") from employee')
        with self.db.engine.connect() as conn:
            result = conn.execute(sql).fetchall()[0][0]
        return result