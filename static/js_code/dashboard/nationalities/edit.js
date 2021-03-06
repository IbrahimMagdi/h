
function check_inputs(id){
    var name_ar = $('input[name="name_ar"]').val();
    var name_en = $('input[name="name_en"]').val();
    if (name_ar.length == 0 || name_en.length == 0) {
        $("button[name=submit]").attr("disabled", "disabled");
    } else {
        $("button[name=submit]").removeAttr("disabled");
    }
}

function update(id){
    var name_ar = $('input[name="name_ar"]').val();
    var name_en = $('input[name="name_en"]').val();
    var status = $('#status:checked').val();
    var submit = document.getElementById("submit");
    var loading = document.getElementById("loading");
    if (submit.style.display === "none") {
        submit.style.display = "block";
        loading.style.display = "none";
        $("name_ar").attr("disabled", false);
        $("name_en").attr("disabled", false);
        $("status").attr("disabled", false);
    } else {
        submit.style.display = "none";
        loading.style.display = "block";
        $("name_ar").attr("disabled", true);
        $("name_en").attr("disabled", true);
        $("status").attr("disabled", true);
    }
    $.ajax({
        type : 'POST',
        url :  "/fun/dashboard/nationalities/edit",
        data: {
            "id": id,
            "name_ar": name_ar,
            "name_en": name_en,
            "status": status,
        },
        success : function(send_object){
            if (send_object.re_status == 104) {
                window.location.href = '/logout';
                $("#public_board_message").fadeIn(1000).delay(4000);
                document.getElementById("public_board_message").innerHTML = send_object.re_message;
                $("#public_board_message").fadeOut(1000).delay(4000);
            } else if (send_object.re_status == 103) {
                submit.style.display = "block";
                loading.style.display = "none";
                $("name_ar").attr("disabled", false);
                $("name_en").attr("disabled", false);
                $("status").attr("disabled", false);
                $("#public_board_message").fadeIn(1000).delay(4000);
                document.getElementById("public_board_message").innerHTML = send_object.re_message;
                $("#public_board_message").fadeOut(1000).delay(4000);
            } else if (send_object.re_status == 201) {
                submit.style.display = "block";
                loading.style.display = "none";
                $("name_ar").attr("disabled", false);
                $("name_en").attr("disabled", false);
                $("status").attr("disabled", false);
                $("#public_board_message").fadeIn(1000).delay(4000);
                document.getElementById("public_board_message").innerHTML = send_object.re_message;
                document.getElementById("item_name").innerHTML = name_ar;
                $("#public_board_message").fadeOut(1000).delay(4000);
            }
        },
        error : function(response){
            submit.style.display = "block";
            loading.style.display = "none";
            $("name_ar").attr("disabled", false);
            $("name_en").attr("disabled", false);
            $("status").attr("disabled", false);
            $("#public_board_message").fadeIn(1000).delay(4000);
            document.getElementById("public_board_message").innerHTML = '???? ???????? ?????????? ??????????????????';
            $("#public_board_message").fadeOut(1000).delay(4000);
        }
    });
}