var $ = jQuery.noConflict();
function listadoSuperficie(){
    $.ajax({
        url:"/Base/Superficie/listar_superficie/",
        type:"get",
        dataType:"json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_superficies')){
                $('#tabla_superficies').DataTable().destroy();
            }
            console.log(response);
            $('#tabla_superficies tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i +1) + '</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td><button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/Base/actualizar_superficie/' + response[i]['pk']+'/\');"> EDITAR </button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton  btn-sm" ';
                fila += 'onclick = "abrir_modal_eliminacion(\'/Base/eliminar_superficie/' + response[i]['pk'] +'/\');"> ELIMINAR </buttton></td>';
                fila += '</tr>';

                $('#tabla_superficies tbody').append(fila);
            }
            $('#tabla_superficies').DataTable({
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
			listadoSuperficie();
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
            listadoSuperficie();
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
        url: '/Base/eliminar_superficie/'+pk+'/',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoSuperficie();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}
$(document).ready(function (){
    listadoSuperficie();
});