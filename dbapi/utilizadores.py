import pyodbc
import json

class Utilizador:

    def obterDriver(self):
        servername='localhost'
        port=1433
        database='PL5SQLProjeto'
        username='PL5SQLProjetoUser'
        password='Pa$$w0rd'
        driver="DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};PORT={};DATABASE={};UID={};PWD={};"
        driver=driver.format(servername,port,database,username,password)
        return driver

    def inserirUtilizador(self,primeiroNome,ultimoNome,morada,codigoPostal,telefone,eMail,password,foto):
        driver=self.obterDriver()
        connection=pyodbc.connect(driver)
        cursor=connection.cursor()
        sqlquery="EXEC dbo.SP_InserirUtilizador ?,?,?,?,?,?,?,?"
        values=(primeiroNome,ultimoNome,morada,codigoPostal,telefone,eMail,password,foto)
        cursor.execute(sqlquery,values)
        result=cursor.fetchall()
        cursor.commit()
        cursor.close()
        connection.close()
        result=json.loads(result[0][0][1:-1])
        return result

    def atualizarUtilizador(self,numeroUtilizador,primeiroNome,ultimoNome,morada,codigoPostal,telefone,eMail,password,foto):
        driver=self.obterDriver()
        connection=pyodbc.connect(driver)
        cursor=connection.cursor()
        sqlquery="EXEC dbo.SP_AtualizarUtilizador ?,?,?,?,?,?,?,?,?"
        values=(numeroUtilizador,primeiroNome,ultimoNome,morada,codigoPostal,telefone,eMail,password,foto)
        cursor.execute(sqlquery,values)
        result=cursor.fetchall()
        cursor.commit()
        cursor.close()
        connection.close()
        result=json.loads(result[0][0][1:-1])
        return result

    def apagarUtilizador(self,numeroUtilizador):
        driver=self.obterDriver()
        connection=pyodbc.connect(driver)
        cursor=connection.cursor()
        sqlquery="EXEC dbo.SP_ApagarUtilizador ?"
        values=(numeroUtilizador)
        cursor.execute(sqlquery,values)
        result=cursor.fetchall()
        cursor.commit()
        cursor.close()
        connection.close()
        result=json.loads(result[0][0][1:-1])
        return result

    def consultarTodosOsUtilizadores(self):
        driver=self.obterDriver()
        connection=pyodbc.connect(driver)
        cursor=connection.cursor()
        sqlquery="EXEC dbo.SP_ConsultarUtilizadores"
        cursor.execute(sqlquery)
        result=cursor.fetchall()
        cursor.close()
        connection.close()
        result=json.loads(result[0][0][1:-1])
        return result

    def consultarUtilizador(self,numeroUtilizador):
        driver=self.obterDriver()
        connection=pyodbc.connect(driver)
        cursor=connection.cursor()
        sqlquery="EXEC dbo.SP_ConsultarUtilizador ?"
        values=(numeroUtilizador)
        cursor.execute(sqlquery,values)
        result=cursor.fetchall()
        cursor.close()
        connection.close()
        result=json.loads(result[0][0][1:-1])
        return result
