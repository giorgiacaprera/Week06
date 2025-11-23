from dao import users_dao
from dao.users_dao import UsersDAO
from dao.user_dto import UserDTO

def main():
    # Usando il pattern DAO, l'applicazione principale non deve conoscere i dettagli
    # del database, nemmeno sapere della sua esistenza: l'accesso al database sarà
    # mediato dalla classe DAO
    users_dao = UsersDAO()

    # Usando il pattern DAO, posso interagire con il database ignorandone l'esistenza,
    # mi basta chiamare i metodi messi a disposizione dalla classe UsersDAO

    #Ad esempio, per inserire un nuovo utente
    # users_dao.addUser(7, "Alessando Gialli", "+12 787878")

    # Oppure passando un oggetto della classe opportuna, se definita
    # u = UserDTO(11, "Luigi Arancioni", "+37 86754512")
    # users_dao.addUser(u)

    # Analogamente per ottenere un elenco lista degli utenti come stringhe o oggetti
    list_users = users_dao.getUsers()
    for user in list_users:
        print(user)

main()