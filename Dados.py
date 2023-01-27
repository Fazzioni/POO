
class Database():
    def __init__(self):
        self.users = []

    def InsertUser(self,user):
        self.users.append(user)
        print("Usuarios:")
        for user in self.users:
            print(user.email)

    def getUser(self,email=None,id=None):
        if not id is None:
            print("Get user: " + str(id))
            for user in self.users:
                if user.id == id:
                    return user
        if not email is None:
            print("Get user: " + email)
            for user in self.users:
                if user.email == email:
                    return user
        return None

