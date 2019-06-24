$(function() {
    $(".btn").on('click', function() {
        myobj = $.get("https://api.noopschallenge.com/hexbot",function(data){
            mycolor = data.colors[0].value
            $(".colorDiv").css("background-color",mycolor)
        })
    })
})