$(document).ready(function(){
  $('.slider').slider();
	$('.modal').modal({
        onOpenStart() {
            if(! window.localStorage.getItem('token')){
              M.toast({
              html: "Please Login!",
              classes: 'light-blue darken-1'
            });
              window.location = '/login'
            }
        },
    });
	$('#create_comment_form').submit(function(e){
		e.preventDefault();
    form = $(this);
    var url = form.attr('action');
    var formData = new FormData(this);
    formData.append('user', localStorage.getItem('user_id'))
		$.ajax({
          type: "POST",
          url: url,
          data: formData,
          processData: false,
          contentType: false,
          headers: {"Authorization": "Token" + " " + window.localStorage.getItem('token')},
          success: function (data) {
            M.toast({
              html: "Successfully Added Your Comment",
              classes: 'light-blue darken-1'
            });
            
            $('#create_comment_modal').modal('close');
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
