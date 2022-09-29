$(document).ready(function(){
    $("#formularioUtilizador").on('shown.bs.modal', function(obj){
        numeroutilizador=$(obj.relatedTarget).data('id');
        ($(obj.relatedTarget).data('action')=='atualizar')?(
            $.get("/consultarutilizador/"+numeroutilizador,function(data,status){
                utilizador=data.Resultado[0]            
                $("#titulonumeroutilizador").html("Utilizador: " +utilizador.NumeroUtilizador);
                $("#numeroutilizador").val(utilizador.NumeroUtilizador);
                $("#primeironome").val(utilizador.PrimeiroNome);
                $("#ultimonome").val(utilizador.UltimoNome);
                $("#morada").val(utilizador.Morada);
                $("#codigopostal").val(utilizador.CodigoPostal);
                $("#telefone").val(utilizador.Telefone);
                $("#email").val(utilizador.EMail);
                $("#username").html("Username: " +utilizador.Username);
                $("#password").val("");
                $("#password2").val("");
                if(utilizador.Foto=='null' || utilizador.Foto==null){
                    $("#foto").attr("src","../static/images/silhueta.png");
                    $("#fotofile").val("silhueta.png");
                }
                else{
                    $("#foto").attr("src","../static/images/"+utilizador.Foto);
                    $("#fotofile").val(utilizador.Foto);
                }
                $("#botaoapagar").show();
                $("#botaoapagar").attr("data-id",utilizador.NumeroUtilizador);
                $("#formularioutilizador").attr("action","/atualizarutilizador")
            })
        ):(
            $("#titulonumeroutilizador").html("Novo Utilizador"),
            $("#numeroutilizador").val(""),
            $("#primeironome").val(""),
            $("#ultimonome").val(""),
            $("#morada").val(""),
            $("#codigopostal").val(""),
            $("#telefone").val(""),
            $("#email").val(""),
            $("#username").html("Username: A definir"),
            $("#foto").attr("src","../static/images/silhueta.png"),
            $("#fotofile").val("silhueta.png"),
            $("#botaoapagar").hide(),
            $("#formularioutilizador").attr("action","/inserirutilizador")
        )
    });
});

function apagar(obj){
    var numeroutilizador=$(obj).attr("data-id");
    $.get("/apagarutilizador/"+numeroutilizador,function(data,status){
        window.location="/utilizadores";
    });
}

function mudarFoto(obj){
    ficheiro=($(obj).val()).replace("C:\\fakepath\\","");
    $("#fileLabel").html(ficheiro);
    $("#fotofile").val(ficheiro);
    $("#foto").attr("src","../static/images/"+ficheiro);
}

