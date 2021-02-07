$(document).ready(function(){
    $('#register_form').submit(function(e){
        e.preventDefault();
    var form = $(this)
    var url = form.attr('action')
        $.ajax({
          type: "POST",
          url: url,
          data: form.serialize(),
          success: function (data) {
            console.log(data)
            if(data['username'] && isArray(data['username'])){
                data['username'].forEach(element => {
                    M.toast({
                    html: "username - " + "" + element,
                    classes: 'light-blue darken-1'
            });
                });
            }
            if(data['password']){
                data['password'].forEach(element => {
                    M.toast({
                    html: "password - " + "" + element,
                    classes: 'light-blue darken-1'
                    });

                });
            }
            if(data['token']){
                window.localStorage.setItem('token', data['token']);
                window.localStorage.setItem('user_id', data['user_id'])
                console.log('token', data['token']);
                M.toast({
                    html: "Successfully Created Account, Redirecting to Login",
                    classes: 'light-blue darken-1'
                    });
                window.location = "/"
            }
            
            
          },
          error: function (xhr, ajaxOptions, thrownError) {
            M.toast({
              html: "Sorry!, Something went wrong, Please try after sometime",
              classes: 'light-blue darken-1'
            });
            }
        });
    });
});