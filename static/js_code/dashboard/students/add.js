function call_army_status(){
    var studentType = $('#student_type option:selected').val();
    var armyStatusView = document.getElementById("army-status-view");
    if (studentType == 0){
        armyStatusView.style.display = "block";
    } else {
        armyStatusView.style.display = "none";
    }
}
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
function call_transfer_status(){
    var recordingType = $('#recording_type option:selected').val();
    var transferStatusView = document.getElementById("transfer-status-view");
    if (recordingType == 1){
        transferStatusView.style.display = "block";
    } else {
        transferStatusView.style.display = "none";
    }
}

function create(){
    var name = $('input[name="name"]').val();
    var national_iD = $('input[name="national_iD"]').val();
    var address = $('input[name="address"]').val();
    var religion = $('#religion option:selected').val();
    var social_status = $('#social_status option:selected').val();
    var date_birth = $('input[name="date_birth"]').val();
    var nationality = $('#nationality option:selected').val();
    var educational_qualification = $('#educational_qualification option:selected').val();
    var total_qualification = $('input[name="total_qualification"]').val();
    var recording_type = $('#recording_type option:selected').val();
    var transfer_destination = $('input[name="transfer_destination"]').val();
    var student_type = $('#student_type option:selected').val();
    var army_status = $('#army_status option:selected').val();
    var systems = $('#systems option:selected').val();
    var teams = $('#teams option:selected').val();
    var phone = $('input[name="phone"]').val();
    var email = $('input[name="email"]').val();

    var submit = document.getElementById("submit");
    var loading = document.getElementById("loading");
    if (submit.style.display === "none") {
        submit.style.display = "block";
        loading.style.display = "none";
    } else {
        submit.style.display = "none";
        loading.style.display = "block";
    }
    $.ajax({
        type : 'POST',
        url :  "/fun/dashboard/students/add",
        data: {
            "name": name,
            "national_iD": national_iD,
            "address": address,
            "religion": religion,
            "social_status": social_status,
            "date_birth": date_birth,
            "nationality": nationality,
            "educational_qualification": educational_qualification,
            "total_qualification": total_qualification,
            "recording_type": recording_type,
            "transfer_destination": transfer_destination,
            "student_type": student_type,
            "army_status": army_status,
            "systems": systems,
            "teams": teams,
            "phone": phone,
            "email": email,
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
                $("#public_board_message").fadeIn(1000).delay(4000);
                document.getElementById("public_board_message").innerHTML = send_object.re_message;
                $("#public_board_message").fadeOut(1000).delay(4000);
            } else if (send_object.re_status == 201) {
                $('#form').trigger("reset");
                submit.style.display = "block";
                loading.style.display = "none";
                $("#public_board_message").fadeIn(1000).delay(4000);
                document.getElementById("public_board_message").innerHTML = send_object.re_message;
                $("#public_board_message").fadeOut(1000).delay(4000);
            }
        },
        error : function(response){
            submit.style.display = "block";
            loading.style.display = "none";
            $("#public_board_message").fadeIn(1000).delay(4000);
            document.getElementById("public_board_message").innerHTML = 'لا يوجد اتصال بالانترنت';
            $("#public_board_message").fadeOut(1000).delay(4000);
        }
    });
}