$(document).ready(function(){

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
	$('#create_blog_form').submit(function(e){
		e.preventDefault();
		form = $(this);
		var url = form.attr('action');
    var formData = new FormData(this);
    formData.append('authors', localStorage.getItem('user_id'))
		$.ajax({
          type: "POST",
          url: url,
          enctype: 'multipart/form-data',
          processData: false,
          contentType: false,
          cache: false,
          timeout: 600000,
          data: formData,
          headers: {"Authorization": "Token" + " " + window.localStorage.getItem('token')},
          success: function (data) {
            M.toast({
              html: "Successfully Created Blog !",
              classes: 'light-blue darken-1'
            });
            M.toast({
              html: "Blog will publish once admin Approve !",
              classes: 'light-blue darken-1'
            });

            $('#create_blog_modal').modal('close');
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