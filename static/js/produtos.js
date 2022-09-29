$(document).ready(function(){
    $("#formularioProduto").on('shown.bs.modal', function(obj){
        numeroproduto=$(obj.relatedTarget).data('id');
        ($(obj.relatedTarget).data('action')=='atualizar')?(
            $.get("/consultarproduto/"+numeroproduto,function(data,status){
                produto=data.Resultado[0]            
                $("#titulonumeroproduto").html("Produto: " +produto.NumeroProduto);
                $("#numeroproduto").val(produto.NumeroProduto);
                $("#designacao").val(produto.Designacao);
                $("#descricao").val(produto.Descricao);
                $("#unidademedida").val(produto.UnidadeMedida);
                $("#precounitario").val(produto.PrecoUnitario);
                $("#taxaiva").val(produto.TaxaIVA);
                if(produto.Foto=='null' || produto.Foto==null){
                    $("#foto").attr("src","../static/images/silhueta.png");
                    $("#fotofile").val("silhueta.png");
                }
                else{
                    $("#foto").attr("src","../static/images/"+produto.Foto);
                    $("#fotofile").val(produto.Foto);
                }
                $("#botaoapagar").show();
                $("#botaoapagar").attr("data-id",produto.NumeroProduto);
                $("#formularioproduto").attr("action","/atualizarproduto")
            })
        ):(
            $("#titulonumeroproduto").html("Novo Produto"),
            $("#numeroproduto").val(""),
            $("#designacao").val(""),
            $("#descricao").val(""),
            $("#unidademedida").val(""),
            $("#precounitario").val(""),
            $("#taxaiva").val(""),
            $("#foto").attr("src","../static/images/silhueta.png"),
            $("#fotofile").val("silhueta.png"),
            $("#botaoapagar").hide(),
            $("#formularioproduto").attr("action","/inserirproduto")
        )
    });
});

function apagar(obj){
    var numeroproduto=$(obj).attr("data-id");
    $.get("/apagarproduto/"+numeroproduto,function(data,status){
        window.location="/produtos";
    });
}

function mudarFoto(obj){
    ficheiro=($(obj).val()).replace("C:\\fakepath\\","");
    $("#fileLabel").html(ficheiro);
    $("#fotofile").val(ficheiro);
    $("#foto").attr("src","../static/images/"+ficheiro);
}

