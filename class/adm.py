from user import user

class Adm(user):

    def __init__(self, name,login, email, pass_hash = None, salt =None):
        # inicializa a classe user
        super().__init__(self, login, email, pass_hash, salt)
        self.name = name
        self.email = email

        
        self.privilege = []
        # estrutura do privilégio não implementado
        raise NotImplementedError


 