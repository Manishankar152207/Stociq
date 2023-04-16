function change_client_status(id){
    $.ajax({
        type : "GET",
        url : "/clients/",
        data : {"changestatus":id},
        success : function(response) {     
            if(response.success == true){     
                 window.location.reload();
            }else{
                swal("Oops!", "Something went wrong", "warning");
            }
        }                        
    });
}

function add_client(){
    csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val()
    console.log(csrfmiddlewaretoken);
    username = $("#username").val();
    password = $("#password").val();
    if (username != '' && password != ''){
        $.ajax({
            type : "POST",
            url : "/clients/",
            data : {"csrfmiddlewaretoken":csrfmiddlewaretoken, "username":username, "password":password},
            success : function(response) {     
                if(response.success == true){     
                     window.location.reload();
                }else{
                    $("#add_usererror").text(response.msg);
                    $("#username").val("");
                    $("#password").val("");
                }
            }                        
        });
    }
    else{
        swal("Oops!", "Username and Password are required field.", "warning");
    }
    
}

function showorderdetails(e){
    $("#modal-username").text($("#"+e.id).attr("data-username"));
    $("#modal-buytime").text($("#"+e.id).attr("data-buytime"));
    $("#modal-buyprice").text($("#"+e.id).attr("data-buyprice"));
    $("#modal-instrument").text($("#"+e.id).attr("data-instrument"));
    $("#modal-qty").text($("#"+e.id).attr("data-qty"));
    $("#modal-buy-status").text($("#"+e.id).attr("data-buy_status"));
    $("#modal-buy-status-message").text($("#"+e.id).attr("data-buy_status_message"));
    $("#modal-selltime").text($("#"+e.id).attr("data-selltime"));
    $("#modal-sellprice").text($("#"+e.id).attr("data-sellprice"));
    $("#modal-sell_status").text($("#"+e.id).attr("data-sell_status"));
    $("#modal-sell-status-message").text($("#"+e.id).attr("data-sell_status_message"));
    $("#modal-diff").text($("#"+e.id).attr("data-diff"));
    $("#modal-pl").text($("#"+e.id).attr("data-profitloss"));
}