from storage.storage import BaseStorage
from storage.model import InputCreateUser
from storage.pg.db import connection


class PgStorage(BaseStorage):

    def __init__(self):
        self.connection = connection

    def save_user(self, user: InputCreateUser, id: str):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO users (user_id, user_name, password, phone_number,  email) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                    (id, user.login, user.password, user.phone_number, user.email))
        self.connection.commit()
        result = cur.fetchone()
        cur.close()
        if result == None:
            raise
        else:
            return {'id': result[0]}

    def delete_user(self, id: str):
        cur = self.connection.cursor()
        cur.execute("DELETE FROM users WHERE user_id = %s RETURNING id;", [id])
        connection.commit()
        result = cur.fetchone()
        cur.close()
        if result == None:
            raise
        else:
            return {'id': result[0]}

    def get_user_by_id(self, id: str):
        cur = connection.cursor()
        cur.execute(
            "SELECT user_name,phone_number, email FROM users WHERE user_id = %s;", [id])
        result = cur.fetchone()
        cur.close()
        if result == None:
            raise
        else:
            return {'id': id, 'login': result[0], 'phone_number': result[1], 'email': result[2]}

    def get_user_by_creds(self, user_name: str, password: str):
        cur = connection.cursor()
        cur.execute(
            "SELECT user_name,phone_number, email FROM users WHERE user_name = %s and password = %s;", [user_name, password])
        result = cur.fetchone()
        cur.close()
        if result == None:
            raise
        else:
            return {'id': id, 'login': result[0], 'phone_number': result[1], 'email': result[2]}

    def save_short_url(self, origin: str, short: str):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO urls (id, origin_url, short_url) VALUES (%s, %s, %s) RETURNING short_url",
                    (id, origin, short))
        self.connection.commit()
        result = cur.fetchone()
        cur.close()
        print(result)
        if result == None:
            raise
        else:
            return {'short_url': result[0]}
