function call_get_teams(){
    var system = $('#systems option:selected').val();
    $.ajax({
        type : 'POST',
        url :  "/fun/dashboard/students/get-teams",
        data: {
            "id": system,
        },
        success : function(send_object){
            if (send_object.re_status == 104) {
                window.location.href = '/logout';
                $("#public_board_message").fadeIn(1000).delay(4000);
                document.getElementById("public_board_message").innerHTML = send_object.re_message;
                $("#public_board_message").fadeOut(1000).delay(4000);
            } else if (send_object.re_status == 201) {
                jQuery('#teams option').remove();
                var teams = document.getElementById("teams");
                for (var item in send_object.re_data) {
                  var id = send_object.re_data[item]['id']
                  var name = send_object.re_data[item]['name']
                  var obj = '<option value="'+id+'">'+name+'</option>'
                  $(teams).append(obj);
                }
            }
        },
        error : function(response){
            $("#public_board_message").fadeIn(1000).delay(4000);
            document.getElementById("public_board_message").innerHTML = 'لا يوجد اتصال بالانترنت';
            $("#public_board_message").fadeOut(1000).delay(4000);
        }
    });
}
