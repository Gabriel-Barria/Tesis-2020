
function editarCentro(){
    activarBoton();
    var data = new FormData($('#form_edicion').get(0));
    $.ajax({
        data: data,
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        cache:false,
        contentType:false,
        processData:false,
       
        success: function (response) {
            
            notificacionSuccess(response.mensaje);
            cerrar_modal_edicion();
            setTimeout('document.location.reload()',900);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);
            activarBoton();
        }
    });
}
