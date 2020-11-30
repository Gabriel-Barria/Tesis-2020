function abrir_modal_login(url){  
    Swal.fire({
            title: 'Debes iniciar sesion primero!',
            text: '',
            icon: 'error'
        })
    $('#login').load(url, function(){
      $(this).modal('show');
    });
  }
function abrir_modal_login_sin_error(url){  
    $('#login').load(url, function(){
      $(this).modal('show');
    });
}

function cerrar_modal_login(){
	  $('#login').modal('hide');

  }
function abrir_modal_register(url) {
	$('#register').load(url, function () {
		$(this).modal('show');
	});
}
function cerrar_modal_register(){
	  $('#register').modal('hide');

}
function registrar_usuario() {
  activarBoton();
  var data = new FormData($('#form_registro').get(0));
  
  $.ajax({
      data: data,
      url: $('#form_registro').attr('action'),
      type: $('#form_registro').attr('method'),
      cache:false,
      contentType:false,
      processData:false,
      success: function (response) {
          notificacionSuccess(response.mensaje);           
          cerrar_modal_register();
         
      },
      error: function (error) {
         notificacionError(error.responseJSON.mensaje); 
         mostrarErroresCreacion(error);
         activarBoton();
          
      }
  });
}