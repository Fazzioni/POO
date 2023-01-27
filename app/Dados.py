import os
import pandas as pd


###  config table
###  id | variable | value


class Database():
    dir = 'Tables'+os.sep

    def teste(self):
        print("teste DB GLOBAL IS OK")

    def __init__(self):
        self.users = []
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        #self.loadTables()
        # carrega as tabelas


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


    def loadTables(self):
        """
            Inicializa todas as tabelas da aplicação
        """
        def Load_table_name(self, name):
            if os.path.exists(Database.dir+ name+'.csv'):
                return pd.read_csv(self.Database+name+'.csv')
            else:
                return pd.DataFrame()

        self.users = Load_table_name(self,'users')
        self.config = Load_table_name(self,'config')

    def __post_tables(self,table_name,table):
        table.to_csv(self.dir+table_name+'.csv',index=False)
    

    def new_id(self,table_name):
        if table_name == 'users':
                pass
            #id = self.config.at[]
                return len(self.users)+1
        else:
            raise Exception("Tabela não encontrada - Não foi possivel gerar um novo id")
    

    #############################
    ## Funcoes da tabela users ##
    #############################
    def post_uesrs(self):
        self.__post_tables('users',self.users)
    
    def InsertUser(self,user):
        self.users.append(user)
        print("Usuarios:")
        for user in self.users:
            print(user.email)
    

