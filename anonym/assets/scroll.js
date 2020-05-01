$(window).scroll(function(e){
    e.preventDefault()
    if($(window).scrollTop() == $(document).height() - $(window).height()){

            $('#post-now').trigger("submit");
            $("#show").show()
            ajaxStart: $("#show").text("LOADING...");

    }
})

$("#butt").click(function(e){
    e.preventDefault()
    console.log(" SOmeone just clicked me")
    $.ajax({
    url:"/user/message/",
    success: function(data){
        alert(data)}

    })

})
$('#post-now').on('submit', function(e){
    e.preventDefault()
    console.log(" form is submittted")
    create_post();

})

function create_post(){
    $.ajax({
        url: "/user/message/",
        type: "POST",
        data:{csrfmiddlewaretoken: document.getElementsByName("csrfmiddlewaretoken")[0].value},
        success: function(json){

            $(".me").hide();
            $("#ben").html($(json).find("#pick"));
            ajaxStop: $("#show").hide()



        },

        error: function(){

            console.log(" an errors occurred")
        },


        })

}