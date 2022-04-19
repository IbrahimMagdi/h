function sign_in_fun(){
    var username = $('input[name="username"]').val();
    var password = $('input[name="password"]').val();
    var submit = document.getElementById("submit");
    var loading = document.getElementById("loading");
    if (submit.style.display === "none") {
        submit.style.display = "block";
        loading.style.display = "none";
    } else {
        loading.style.display = "block";
        submit.style.display = "none";
    }
    $.ajax({
        type : 'POST',
        url :  "/fun/website/login",
        data : {
            'username' : username,
            'password' : password,
        },
        success : function(send_object){
            if (send_object.re_status == 104) {
                window.location.href = '/logout';
                $("#public_message").fadeIn(1000).delay(4000);
                document.getElementById("public_message").innerHTML = send_object.re_message;
                $("#public_message").fadeOut(1000).delay(4000);
                submit.style.display = "block";
                loading.style.display = "none";
            } else if (send_object.re_status == 103) {
                $("#public_message").fadeIn(1000).delay(4000);
                document.getElementById("public_message").innerHTML = send_object.re_message;
                $("#public_message").fadeOut(1000).delay(4000);
                submit.style.display = "block";
                loading.style.display = "none";
            } else if (send_object.re_status == 201) {
                $("#public_message").fadeIn(1000).delay(4000);
                document.getElementById("public_message").innerHTML = send_object.re_message;
                $("#public_message").fadeOut(1000).delay(4000);
                submit.style.display = "block";
                loading.style.display = "none";
                window.location.href = send_object.re_data;
            }
        },
        error : function(response){
            $("#public_message").fadeIn(1000).delay(4000);
            document.getElementById("public_message").innerHTML = 'Error in internet!';
            $("#public_message").fadeOut(1000).delay(4000);
            submit.style.display = "block";
            loading.style.display = "none";
        }
    });
}
