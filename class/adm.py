class Adm():
    def __init__(self, name_adm, pass_hash, email):
        self.nameADM = name_adm
        self.pass_hash = pass_hash
        self.email = email

    def check_pass(self,hash):
        pass