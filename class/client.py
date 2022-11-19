from user import user


class Client(user):
    def __init__(self, code, social_name, cpfj, login, email, pass_hash = None, salt =None):
        # inicializa a classe user
        super().__init__(self, login, email, pass_hash, salt)
        self.code = code
        self.social_name = social_name
        self.cpfj = cpfj