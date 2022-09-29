from flask import Flask,render_template,request,redirect,url_for,session
from dbapi.clientes import Cliente
from dbapi.fornecedores import Fornecedor
from dbapi.produtos import Produto
from dbapi.utilizadores import Utilizador
from dbapi.autenticacao import Autenticacao
from dbapi.newsletter import Newsletter

app=Flask(__name__)
app.secret_key="k4QtZWvoB9NnNnJrbv4SpSC2wtw7NHCwSekUXgqDoyuUgYiYe5UbzuJj7Xwe4jNZa3YjUorWAspAa85G7DoPAhWvkdCn4W6LsD6EnU8Nnam7baX8iHiWASpKzqMTU9UJ"

@app.route('/')
def inicio():
    session["Page"]="inicio.html"
    autenticacao=Autenticacao()
    if(session.get("ChaveSessao") is None or autenticacao.verificarSessao(session.get("ChaveSessao"))["ErrorCode"]!=0):
        session["ChaveSessao"]="00000000-0000-0000-0000-000000000000"
        session["Nome"]=""
        session["Foto"]=""
    return render_template('inicio.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/loja')
def loja():
    return render_template('loja.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/perfil')
def perfil():
    session["Page"]="perfil.html"
    autenticacao=Autenticacao()
    if(session.get("ChaveSessao") is None or autenticacao.verificarSessao(session.get("ChaveSessao"))["ErrorCode"]!=0):
        return render_template('login.html')
    return render_template('perfil.html')

@app.route('/gestao')
def gestao():
    session["Page"]="gestao.html"
    autenticacao=Autenticacao()
    if(session.get("ChaveSessao") is None or autenticacao.verificarSessao(session.get("ChaveSessao"))["ErrorCode"]!=0):
        return render_template('login.html')
    return render_template('gestao.html')

@app.route('/clientes')
def clientes():
    session["Page"]="clientes.html"
    autenticacao=Autenticacao()
    if(session.get("ChaveSessao") is None or autenticacao.verificarSessao(session.get("ChaveSessao"))["ErrorCode"]!=0):
        return render_template('login.html')
    cliente=Cliente()
    resultado=cliente.consultarTodosOsClientes()
    return render_template('clientes.html',data=resultado)

@app.route('/consultarcliente/<numerocliente>')
def consultarcliente(numerocliente):
    cliente=Cliente()
    data=cliente.consultarCliente(numerocliente)
    return data

@app.route("/inserircliente",methods=["POST"])
def inserircliente():
    Nome=request.form["nome"]
    NIF=request.form["nif"]
    Morada=request.form["morada"]
    CodigoPostal=request.form["codigopostal"]
    Telefone=request.form["telefone"]
    Email=request.form["email"]
    Foto=request.form["fotofile"]
    cliente=Cliente()
    resultado=cliente.inserirCliente(Nome,NIF,Morada,CodigoPostal,Telefone,Email,Foto)
    return redirect(url_for("clientes"))

@app.route("/atualizarcliente",methods=["POST"])
def atualizarcliente():
    NumeroCliente=request.form["numerocliente"]
    Nome=request.form["nome"]
    NIF=request.form["nif"]
    Morada=request.form["morada"]
    CodigoPostal=request.form["codigopostal"]
    Telefone=request.form["telefone"]
    Email=request.form["email"]
    Foto=request.form["fotofile"]
    cliente=Cliente()
    resultado=cliente.atualizarCliente(NumeroCliente,Nome,NIF,Morada,CodigoPostal,Telefone,Email,Foto)
    return redirect(url_for("clientes"))

@app.route('/apagarcliente/<numerocliente>')
def apagarcliente(numerocliente):
    cliente=Cliente()
    data=cliente.apagarCliente(numerocliente)
    return data

@app.route('/fornecedores')
def fornecedores():
    session["Page"]="fornecedores.html"
    autenticacao=Autenticacao()
    if(session.get("ChaveSessao") is None or autenticacao.verificarSessao(session.get("ChaveSessao"))["ErrorCode"]!=0):
        return render_template('login.html')
    fornecedor=Fornecedor()
    resultado=fornecedor.consultarTodosOsFornecedores()
    return render_template('fornecedores.html',data=resultado)

@app.route('/consultarfornecedor/<numerofornecedor>')
def consultarfornecedor(numerofornecedor):
    fornecedor=Fornecedor()
    data=fornecedor.consultarFornecedor(numerofornecedor)
    return data

@app.route("/inserirfornecedor",methods=["POST"])
def inserirfornecedor():
    Nome=request.form["nome"]
    NIPC=request.form["nipc"]
    Morada=request.form["morada"]
    CodigoPostal=request.form["codigopostal"]
    Telefone=request.form["telefone"]
    Email=request.form["email"]
    fornecedor=Fornecedor()
    resultado=fornecedor.inserirFornecedor(Nome,NIPC,Morada,CodigoPostal,Telefone,Email)
    return redirect(url_for("fornecedores"))

@app.route("/atualizarfornecedor",methods=["POST"])
def atualizarfornecedor():
    NumeroFornecedor=request.form["numerofornecedor"]
    print(NumeroFornecedor)
    Nome=request.form["nome"]
    NIPC=request.form["nipc"]
    Morada=request.form["morada"]
    CodigoPostal=request.form["codigopostal"]
    Telefone=request.form["telefone"]
    Email=request.form["email"]
    fornecedor=Fornecedor()
    resultado=fornecedor.atualizarFornecedor(NumeroFornecedor,Nome,NIPC,Morada,CodigoPostal,Telefone,Email)
    return redirect(url_for("fornecedores"))

@app.route('/apagarfornecedor/<numerofornecedor>')
def apagarfornecedor(numerofornecedor):
    fornecedor=Fornecedor()
    data=fornecedor.apagarFornecedor(numerofornecedor)
    return data

@app.route('/produtos')
def produtos():
    session["Page"]="produtos.html"
    autenticacao=Autenticacao()
    if(session.get("ChaveSessao") is None or autenticacao.verificarSessao(session.get("ChaveSessao"))["ErrorCode"]!=0):
        return render_template('login.html')
    produto=Produto()
    resultado=produto.consultarTodosOsProdutos()
    return render_template('produtos.html',data=resultado)

@app.route('/consultarproduto/<numeroproduto>')
def consultarproduto(numeroproduto):
    produto=Produto()
    data=produto.consultarProduto(numeroproduto)
    return data

@app.route("/inserirproduto",methods=["POST"])
def inserirproduto():
    Designacao=request.form["designacao"]
    Descricao=request.form["descricao"]
    UnidadeMedida=request.form["unidademedida"]
    PrecoUnitario=request.form["precounitario"]
    TaxaIVA=request.form["taxaiva"]
    Foto=request.form["fotofile"]
    produto=Produto()
    resultado=produto.inserirProduto(Designacao,Descricao,UnidadeMedida,PrecoUnitario,TaxaIVA,Foto)
    return redirect(url_for("produtos"))

@app.route("/atualizarproduto",methods=["POST"])
def atualizarproduto():
    NumeroProduto=request.form["numeroproduto"]
    Designacao=request.form["designacao"]
    Descricao=request.form["descricao"]
    UnidadeMedida=request.form["unidademedida"]
    PrecoUnitario=request.form["precounitario"]
    TaxaIVA=request.form["taxaiva"]
    Foto=request.form["fotofile"]
    produto=Produto()
    resultado=produto.atualizarProduto(NumeroProduto,Designacao,Descricao,UnidadeMedida,PrecoUnitario,TaxaIVA,Foto)
    return redirect(url_for("produtos"))

@app.route('/apagarproduto/<numeroproduto>')
def apagarproduto(numeroproduto):
    produto=Produto()
    data=produto.apagarProduto(numeroproduto)
    return data

@app.route('/utilizadores')
def utilizadores():
    session["Page"]="utilizadores.html"
    autenticacao=Autenticacao()
    if(session.get("ChaveSessao") is None or autenticacao.verificarSessao(session.get("ChaveSessao"))["ErrorCode"]!=0):
        return render_template('login.html')
    utilizador=Utilizador()
    resultado=utilizador.consultarTodosOsUtilizadores()
    return render_template('utilizadores.html',data=resultado)

@app.route('/consultarutilizador/<numeroutilizador>')
def consultarutilizador(numeroutilizador):
    utilizador=Utilizador()
    data=utilizador.consultarUtilizador(numeroutilizador)
    return data

@app.route("/inserirutilizador",methods=["POST"])
def inserirutilizador():
    PrimeiroNome=request.form["primeironome"]
    UltimoNome=request.form["ultimonome"]
    Morada=request.form["morada"]
    CodigoPostal=request.form["codigopostal"]
    Telefone=request.form["telefone"]
    Email=request.form["email"]
    Password=request.form["password"]
    Foto=request.form["fotofile"]
    utilizador=Utilizador()
    resultado=utilizador.inserirUtilizador(PrimeiroNome,UltimoNome,Morada,CodigoPostal,Telefone,Email,Password,Foto)
    return redirect(url_for("utilizadores"))

@app.route("/atualizarutilizador",methods=["POST"])
def atualizarutilizador():
    NumeroUtilizador=request.form["numeroutilizador"]
    PrimeiroNome=request.form["primeironome"]
    UltimoNome=request.form["ultimonome"]
    Morada=request.form["morada"]
    CodigoPostal=request.form["codigopostal"]
    Telefone=request.form["telefone"]
    Email=request.form["email"]
    Password=request.form["password"]
    Foto=request.form["fotofile"]
    utilizador=Utilizador()
    resultado=utilizador.atualizarUtilizador(NumeroUtilizador,PrimeiroNome,UltimoNome,Morada,CodigoPostal,Telefone,Email,Password,Foto)
    return redirect(url_for("utilizadores"))

@app.route('/apagarutilizador/<numeroutilizador>')
def apagarutilizador(numeroutilizador):
    utilizador=Utilizador()
    data=utilizador.apagarUtilizador(numeroutilizador)
    return data

@app.route('/inserirEmailNewsletter/<email>')
def inserirEmailNewsletter(email):
    newsletter=Newsletter()
    data=newsletter.inserirEMailNewsletter(email)
    return data

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    autenticacao=Autenticacao()
    autenticacao.logout(session.get("ChaveSessao"))
    session["ChaveSessao"]="00000000-0000-0000-0000-000000000000"
    session["Nome"]=""
    session["Foto"]=""
    return render_template('inicio.html')

@app.route('/authenticate',methods=["POST"])
def authenticate():
    Username=request.form["username"]
    Password=request.form["password"]
    print(Username)
    print(Password)
    autenticacao=Autenticacao()
    resultado=autenticacao.login(Username,Password)
    print(resultado)
    if resultado['ErrorCode']==0:
        session["ChaveSessao"]=resultado["SessionData"][0]["ChaveSessao"]
        session["Nome"]=resultado["SessionData"][0]["Nome"]
        session["Foto"]=resultado["SessionData"][0]["Foto"]
        return render_template(session["Page"])
    else:
        session["ChaveSessao"]="00000000-0000-0000-0000-000000000000"
        session["Nome"]=""
        session["Foto"]=""
        return render_template('login.html')

@app.route('/recuperarpassword')
def recuperarpassword():
    return render_template('recuperarpassword.html')

@app.route('/mensagemenviada')
def mensagemenviada():
    return render_template('mensagemenviada.html')

@app.route('/novapassword')
def novapassword():
    return render_template('novapassword.html')

@app.route('/passwordalterada')
def passwordalterada():
    return render_template('passwordalterada.html')

@app.route('/novoutilizador')
def novoutilizador():
    return render_template('novoutilizador.html')

@app.route('/ativeasuaconta')
def ativeasuaconta():
    return render_template('ativeasuaconta.html')

@app.route('/contaativada')
def contaativada():
    return render_template('contaativada.html')

if __name__=='__main__':
    app.debug=True
    app.run("localhost","80")