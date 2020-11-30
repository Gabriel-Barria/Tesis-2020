var $ = jQuery.noConflict();
function seleccionar_cancha(url){ 
          
    $('#contenedor-calendario').load(url, function(){
        $('#custom-content-below-messages-tab').click();
        $(this).load('html');

    });
    $('#custom-content-below-messages-tab').on('shown.bs.tab', function (e) {
        console.log('se acaba de seleccionar la pestaña del calendario')
        // TODO: check href of e.target to detect your tab
        $('#calendar').render;
    });
   
      

    }
    function registrar(){
        $.ajax({
            data: $('#form_creacion').serialize(),
            url:  $('#form_creacion').attr('action'),
            type: $('#form_creacion').attr('method'),
            success: function(response){
                $('#myModal').modal('hide');
                notificacionSuccess(response.mensaje);
                seleccionar_cancha($('#form_creacion').attr('name'));
                

                
            },	
            error: function(error){
                notificacionError(error.responseJSON.mensaje); 
                mostrarErroresCreacion(error);
                console.log(error);
                
            }
        });
    }

