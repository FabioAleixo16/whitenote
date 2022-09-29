import pyodbc
import json

class Pesquisa:

    def obterDriver(self):
        servername='localhost'
        port=1433
        database='PL5SQLProjeto'
        username='PL5SQLProjetoUser'
        password='Pa$$w0rd'
        driver="DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};PORT={};DATABASE={};UID={};PWD={};"
        driver=driver.format(servername,port,database,username,password)
        return driver

    def pesquisar(self, pesquisa):
        driver=self.obterDriver()
        connection=pyodbc.connect(driver)
        cursor=connection.cursor()
        sqlquery="EXEC dbo.SP_Pesquisar ?"
        values=(pesquisa)
        cursor.execute(sqlquery,values)
        result=cursor.fetchall()
        cursor.close()
        connection.close()
        result=json.loads(result[0][0][1:-1])
        return result