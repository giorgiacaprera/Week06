import mysql.connector

# localhost oppure 127.0.0.1 significano calcolatore locale
# cnx = mysql.connector.connect(user='root',
#                               password='',
#                               host='localhost',
#                               database='pa')

cnx = mysql.connector.connect(option_files="db.cnf")
cursor = cnx.cursor()
query_insert = """INSERT INTO User
                  (id, name, phone)
                  VALUE (%s,%s,%s)"""

#cursor.execute(query_insert, (6, "Anna Blu", "+38 1111111"))
#cnx.commit()

query_update = """UPDATE User
                  SET phone = %s
                  WHERE name = %s"""
cursor.execute(query_update, ("+33 3333333", "Anna Blu"))
cnx.commit()

query_delete = """DELETE FROM User
                  WHERE id = %s
               """
cursor.execute(query_delete, (5, )) # , serve per evitare errore con un solo parametro
cnx.commit()

cursor = cnx.cursor(dictionary=True)
query_read = """SELECT * FROM User""" # Eventualmente con parametri
cursor.execute(query_read) # Non serve il commit() perchè non modifico il database

#for row in cursor:
#    print(row["name"]+", "+row["phone"])

row = cursor.fetchone() # Una riga alla volta
while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.close()
cnx.close()