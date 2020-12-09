var $ = jQuery.noConflict();
function seleccionar_cancha(url){ 
          
    $('#contenedor-calendario').load(url, function(){
        $('#custom-content-below-messages-tab').click();
        
        $(this).load('html',function(){
            $('.fc-timeGridThreeDay-button').hide();
            
            
        });
        
        
        
        

    });

    $('#custom-content-below-messages-tab').on('shown.bs.tab', function (e) {
        $('.fc-timeGridThreeDay-button').click();
        
        
        
    });
   
      

    }
    function registrar(){
        var data = new FormData($('#form_creacion').get(0));
    
                $.ajax({
                    data: data,
                    url: $('#form_creacion').attr('action'),
                    type: $('#form_creacion').attr('method'),
                    cache:false,
                    contentType:false,
                    processData:false,
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
    function actualizar_tabla(){
        $('#contenedor-calendario').updateSize();
    }

