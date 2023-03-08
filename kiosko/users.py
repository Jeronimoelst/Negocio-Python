from kiosko.excelfIle import readFileSheet

class Users:
    def __init__(self):
        pass


    def isAuthenticated(self, userName, password):
        usuarios = readFileSheet("Usuario")
        flag= False
        for usuario in usuarios.itertuples(index=False):
            usuario_db = usuario[1]
            pass_db = usuario[2]
            if  usuario_db == str(userName) and password == str(pass_db):
                flag = True
                break
        return flag    
