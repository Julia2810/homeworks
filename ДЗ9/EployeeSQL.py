from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.sql import text




class Table:
    
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

# получение списка компаний
    def get_companies(self):
        sql = text("select * from company")
        with self.db.engine.connect() as conn:
            result = conn.execute(sql).fetchall()
        return result
    
    
# получение списка сотрудников одной компании  
    def get_list_employee(self, id):
        sql = text("select * from employee where id =:company_id")
        with self.db.engine.connect() as conn:
            result = conn.execute(sql, company_id = id).fetchall()
        return result
    
    
# добавление одного сотрудника
    def add_employee(self, first_name, last_name, middle_name, phone, url, id):
        sql = text("insert into employee (\"first_name\", \"last_name\", \"middle_name\", \"phone\", \"avatar_url\", \"companyId\") values (:new_first_name, :new_last_name, :new_middle_name, :new_phone, :new_avatar_url, :company_id)")
        with self.db.engine.connect() as conn:
            result = conn.execute(sql, new_first_name = first_name, new_last_name = last_name, new_middle_name = middle_name, new_phone = phone, new_avatar_url = url, company_id = id).fetchall()
        return result
    
    
# удаление одного сотрудника по id
    def delete_employee(self, id):
        sql = text("delete from employee where id =:employee_id")
        with self.db.engine.connect() as conn:
            result = conn.execute(sql, employee_id = id).fetchall()
        return result
    
    
# получение id вновь созданного сотрудника  
    def get_max_id(self):
        sql = text("select MAX(id) from employee")
        with self.db.engine.connect() as conn:
            result = conn.execute(sql).fetchall()
        return result

