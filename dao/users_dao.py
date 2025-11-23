import mysql.connector

from dao.database_connect import DatabaseConnect
from dao.user_dto import UserDTO

# Classe che si occupa di rendere "trasparente" l'accesso al database
class UsersDAO:
    def __init__(self): # Eventualmente apertura e chiusura della connessione in una altra classe ancora
        self._database_connect = DatabaseConnect()

    # Metodo DAO per aggiungere una riga alla tabella User
    def addUser(self, u): #id, name, phone
        cnx = self._database_connect.get_connection()
        cursor = cnx.cursor()
        query = """INSERT INTO User 
                   (id, name, phone) 
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (u.id, u.name, u.phone))
        cnx.commit()
        cursor.close()
        cnx.close()

    # Metodo DAO per ottenere tutte le righe della tabella User
    def getUsers(self):
        cnx = self._database_connect.get_connection()
        cursor = cnx.cursor()
        query = """SELECT * FROM User"""
        cursor.execute(query)

        result = []
        for row in cursor:
            uTemp = UserDTO(row[0], row[1], row[2])
            result.append(uTemp)

        cursor.close()
        cnx.close()
        return result