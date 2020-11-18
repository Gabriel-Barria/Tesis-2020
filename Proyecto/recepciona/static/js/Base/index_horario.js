var $ = jQuery.noConflict();
function listadoHorario(){
    $.ajax({
        url:"/Base/Horario/listar_horario/",
        type:"get",
        dataType:"json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_horarios')){
                $('#tabla_horarios').DataTable().destroy();
            }
            console.log(response);
            $('#tabla_horarios tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i +1) + '</td>';
                fila += '<td>' + response[i]["fields"]['hora_inicio'] + '</td>';
                fila += '<td>' + response[i]["fields"]['hora_termino'] + '</td>';
                fila += '<td>' + response[i]["fields"]['dia'] + '</td>';                
                fila += '<td><button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/Base/actualizar_horarios/' + response[i]['pk']+'/\');"> EDITAR </button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton  btn-sm" ';
                fila += 'onclick = "abrir_modal_eliminacion(\'/Base/eliminar_horario/' + response[i]['pk'] +'/\');"> ELIMINAR </buttton></td>';
                fila += '</tr>';

                $('#tabla_horarios tbody').append(fila);
            }
            $('#tabla_horarios').DataTable({
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
			listadoHorario();
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
            listadoHorario();
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
        url: '/Base/eliminar_horario/'+pk+'/',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoHorario();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}
$(document).ready(function (){
    listadoHorario();
});