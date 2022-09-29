function inserirEmailNewsletter(){
    var email=$("#emailnewsletter").val();
    $.get("/inserirEmailNewsletter/"+email,function(data,status){
        mensagem=data.ErrorMessage;
        $("#alerta").html(mensagem);
        if(data.ErrorCode==0){
            $("#alert").removeClass("alert-danger");
            $("#alert").addClass("alert-success");
        }
        else
        {
            $("#alert").removeClass("alert-success");
            $("#alert").addClass("alert-danger");
        }
       
        $("#alert").fadeIn();
    });
}
