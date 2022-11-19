class user():
    def __init__(self, login, email, pass_hash = None, salt =None):
        self.login = login
        self.email = email
        self.pass_hash = pass_hash
        self.salt = salt
    

    def check_pass(self, hash):
        pass


    def change_pass(self, new_pass):
        pass
