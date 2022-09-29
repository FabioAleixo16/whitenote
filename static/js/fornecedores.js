$(document).ready(function(){
    $("#formularioFornecedor").on('shown.bs.modal', function(obj){
        numerofornecedor=$(obj.relatedTarget).data('id');
        ($(obj.relatedTarget).data('action')=='atualizar')?(
            $.get("/consultarfornecedor/"+numerofornecedor,function(data,status){
                fornecedor=data.Resultado[0]            
                $("#titulonumerofornecedor").html("Fornecedor: " +fornecedor.NumeroFornecedor);
                $("#numerofornecedor").val(fornecedor.NumeroFornecedor);
                $("#nome").val(fornecedor.Nome);
                $("#nipc").val(fornecedor.NIPC);
                $("#morada").val(fornecedor.Morada);
                $("#codigopostal").val(fornecedor.CodigoPostal);
                $("#telefone").val(fornecedor.Telefone);
                $("#email").val(fornecedor.EMail);
                $("#botaoapagar").show();
                $("#botaoapagar").attr("data-id",fornecedor.NumeroFornecedor);
                $("#formulariofornecedor").attr("action","/atualizarfornecedor")
            })
        ):(
            $("#titulonumerofornecedor").html("Novo Fornecedor"),
            $("#numerofornecedor").val(""),
            $("#nome").val(""),
            $("#nipc").val(""),
            $("#morada").val(""),
            $("#codigopostal").val(""),
            $("#telefone").val(""),
            $("#email").val(""),
            $("#botaoapagar").hide(),
            $("#formulariofornecedor").attr("action","/inserirfornecedor")
        )
    });
});

function apagar(obj){
    var numerofornecedor=$(obj).attr("data-id");
    $.get("/apagarfornecedor/"+numerofornecedor,function(data,status){
        window.location="/fornecedores";
    });
}


