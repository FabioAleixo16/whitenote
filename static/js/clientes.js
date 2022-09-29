$(document).ready(function(){
    $("#formularioCliente").on('shown.bs.modal', function(obj){
        numerocliente=$(obj.relatedTarget).data('id');
        ($(obj.relatedTarget).data('action')=='atualizar')?(
            $.get("/consultarcliente/"+numerocliente,function(data,status){
                cliente=data.Resultado[0]            
                $("#titulonumerocliente").html("Cliente: " +cliente.NumeroCliente);
                $("#numerocliente").val(cliente.NumeroCliente);
                $("#nome").val(cliente.Nome);
                $("#nif").val(cliente.NIF);
                $("#morada").val(cliente.Morada);
                $("#codigopostal").val(cliente.CodigoPostal);
                $("#telefone").val(cliente.Telefone);
                $("#email").val(cliente.EMail);
                if(cliente.Foto=='null' || cliente.Foto==null){
                    $("#foto").attr("src","../static/images/silhueta.png");
                    $("#fotofile").val("silhueta.png");
                }
                else{
                    $("#foto").attr("src","../static/images/"+cliente.Foto);
                    $("#fotofile").val(cliente.Foto);
                }
                $("#botaoapagar").show();
                $("#botaoapagar").attr("data-id",cliente.NumeroCliente);
                $("#formulariocliente").attr("action","/atualizarcliente")
            })
        ):(
            $("#titulonumerocliente").html("Novo Cliente"),
            $("#numerocliente").val(""),
            $("#nome").val(""),
            $("#nif").val(""),
            $("#morada").val(""),
            $("#codigopostal").val(""),
            $("#telefone").val(""),
            $("#email").val(""),
            $("#foto").attr("src","../static/images/silhueta.png"),
            $("#fotofile").val("silhueta.png"),
            $("#botaoapagar").hide(),
            $("#formulariocliente").attr("action","/inserircliente")
        )
    });
});

function apagar(obj){
    var numerocliente=$(obj).attr("data-id");
    $.get("/apagarcliente/"+numerocliente,function(data,status){
        window.location="/clientes";
    });
}

function mudarFoto(obj){
    ficheiro=($(obj).val()).replace("C:\\fakepath\\","");
    $("#fileLabel").html(ficheiro);
    $("#fotofile").val(ficheiro);
    $("#foto").attr("src","../static/images/"+ficheiro);
}

