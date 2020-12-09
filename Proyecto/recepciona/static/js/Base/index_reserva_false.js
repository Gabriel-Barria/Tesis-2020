var $ = jQuery.noConflict();
function listadoReservaFalse(){
    $.ajax({
        url:"/Base/Reserva/listar_reserva_false/",
        type:"get",
        dataType:"json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_reservas_false')){
                $('#tabla_reservas_false').DataTable().destroy();
            }
            console.log(response);
            $('#tabla_reservas_false tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i +1) + '</td>';
                fila += '<td>' + response[i]["fields"]['usuario'] + '</td>';
                fila += '<td>' + response[i]["fields"]['cancha'] + '</td>';
                fila += '<td>' + response[i]["fields"]['date_start'] + '</td>';
                fila += '<td>' + response[i]["fields"]['date_end'] + '</td>';
                fila += '<td><div class="round-img"><img class="rounded-circle" onclick="mostrar_imagen(\'/Base/comprobante/' + response[i]['pk']+'/\');" src="/media/'+response[i]["fields"]['comprobante']+'" alt=""></div></td>';
                fila += '<td><button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/Base/actualizar_reserva_false/' + response[i]['pk']+'/\');">CONFIRMAR</button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton  btn-sm" ';
                fila += 'onclick = "abrir_modal_eliminacion(\'/Base/eliminar_reserva_false/' + response[i]['pk'] +'/\');"> ELIMINAR </buttton></td>';
                fila += '</tr>';

                $('#tabla_reservas_false tbody').append(fila);
            }
            $('#tabla_reservas_false').DataTable({
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                    infoFiltered: "(Filtrado de _MAX_ total entradas)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar _MENU_ Entradas",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados encontrados",
                    paginate: {
                      first: "Primero",
                      last: "Ultimo",
                      next: "Siguiente",
                      previous: "Anterior",
                    },
                  },
            });
        },
        error: function(error){
            console.log(error);
        }

    });
}
function registrar(){
	$.ajax({
		data: $('#form_creacion').serialize(),
		url:  $('#form_creacion').attr('action'),
		type: $('#form_creacion').attr('method'),
		success: function(response){
			notificacionSuccess(response.mensaje);
			listadoReserva();
			cerrar_modal_creacion();
		},	
		error: function(error){
            notificacionError(error.responseJSON.mensaje); 
            mostrarErroresCreacion(error);
			console.log(error);
			
		}
	});
}
function editar(){
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
            listadoReservaFalse();
            cerrar_modal_edicion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);
            activarBoton();
        }
    });
}
function eliminar(pk) {
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/Base/eliminar_reserva_false/'+pk+'/',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoReservaFalse();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}
function mostrar_imagen(url){    
    $('#comprobante').load(url, function(){
      $(this).modal('show');
    });
  }
function cerrar_modal(){
	$('#comprobante').modal('hide');
	
}
$(document).ready(function (){
    listadoReservaFalse();
});