$('#post-form').on('submit', function(event){

    console.log(" form is submittted")
    create_post();

})

function create_post(){
    console.log("post is working")
    $.ajax({
        url: "/user/login/",
        type: "POST",
        data:{username: $("#id_username").val(),
              password:$("#id_password").val(),
              csrfmiddlewaretoken: document.getElementsByName("csrfmiddlewaretoken")[0].value},


        success: function(json){

            console.log(json)
        },
        error: function(){

            console.log(" an error occurred")
        },

    })
}




$("#textarea").keyup(function(){
    $("#count").text("Characters left: "+(200 - $(this).val().length));
    if($(this).val().length > 200){
        $(this).val($(this).val().substring(0,200));
    }
});

$('#post-now').on('submit', function(event){
    event.preventDefault()
    console.log(" form is submittted")
    create_pst();

})


function create_pst(){
    console.log("post is working")
    $.ajax({
        url: "/user/",
        type: "POST",
        data:{
              message:$("#textarea").val(),
              csrfmiddlewaretoken: document.getElementsByName("csrfmiddlewaretoken")[0].value},


        success: function(json){
            $("#textarea").val(" ");
            $("#Update").text("Message sent!");
        },
        error: function(){

            console.log(" Error")

        },

    })
}



