$(document).ready(function(){
	$('#login_form').submit(function(e){
		e.preventDefault();
    var form = $(this)
    var url = form.attr('action')
		$.ajax({
          type: "POST",
          url: url,
          data: form.serialize(),
          success: function (data) {
            localStorage.setItem('token', data['token']);
            localStorage.setItem('username', data['username']);
            localStorage.setItem('user_id', data['user_id']);
            M.toast({
              html: "Successfully Added Your Comment",
              classes: 'light-blue darken-1'
            });
            window.location = "/"
          },
          error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr, ajaxOptions, thrownError)

          if(xhr.responseJSON['non_field_errors']){
                xhr.responseJSON['non_field_errors'].forEach(element => {
                    M.toast({
                    html: element,
                    classes: 'light-blue darken-1'
                    });
                    M.toast({
                    html: "please Check credentials or Register",
                    classes: 'light-blue darken-1'
                    });

                });
            }
          else{
            M.toast({
              html: "Sorry!, Something went wrong, Please try after sometime",
              classes: 'light-blue darken-1'
            });

          }
      		}
        });
	});
});