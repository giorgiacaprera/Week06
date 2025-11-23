import mysql.connector

class DatabaseConnect():
    def __init__(self):
        _cnx = None

    def get_connection(self):
        try:
            self._cnx = mysql.connector.connect(user='root',
                                                password='',
                                                host='127.0.0.1',
                                                database='pa')
            return self._cnx
        except mysql.connector.Error as err:
            print(err)
            return None

    #def close_connection(self):
    #    self._cnx.close()