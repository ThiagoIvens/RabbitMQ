class User(object):

    def __init__(self, idusuario = 0, usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):

        banco = DataBaseSqlite()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into usuarios (usuario, senha) values ('" + self.usuario + "', '" + self.senha + "')")
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = DataBaseSqlite()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set usuario = '" + self.usuario + "', senha = '" + self.senha +
            "' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        banco =  DataBaseSqlite()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco =  DataBaseSqlite()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = " + idusuario + "  ")

            for linha in c:
                self.usuario = linha[1]
                self.senha = linha[2]
            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"


    def selectAllUsers(self):
        banco = DataBaseSqlite()
        try:

            c = banco.conexao.cursor()

            users = c.execute("select * from usuarios").fetchall()

            for linha in c:
                self.usuario = linha[1]
                self.senha = linha[2]
            c.close()

            return users
        except:
            return "Usuário não encontrado."

# sqlite -----------------------------------------------------------------------------
import sqlite3

class DataBaseSqlite():
    def __init__(self):
        self.conexao = sqlite3.connect('sqlite.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                    idusuario integer primary key autoincrement,
                    usuario text,
                    senha text)""")
        self.conexao.commit()
        c.close()