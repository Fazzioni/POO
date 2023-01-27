


class user():
    ids = 0

    def new_id():
        user.ids += 1
        return user.ids

    def __init__(self, email,password, name) -> None:
        self.email = email
        self.password = password
        self.name = name
        self.is_active = True
        self.id = user.new_id()
        self.autenticado = False;

    def get_id(self):
        return self.id
    
    def is_authenticated(self):
        return self.autenticado


