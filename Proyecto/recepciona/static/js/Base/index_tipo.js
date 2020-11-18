var $ = jQuery.noConflict();
function listadoTipo(){
    $.ajax({
        url:"/Base/Tipo_Cancha/listar_tipo/",
        type:"get",
        dataType:"json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_tipos')){
                $('#tabla_tipos').DataTable().destroy();
            }
            console.log(response);
            $('#tabla_tipos tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i +1) + '</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td><button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/Base/actualizar_tipo/' + response[i]['pk']+'/\');"> EDITAR </button>';
                fila += '<button type = "button" class = "btn btn-danger tableButton  btn-sm" ';
                fila += 'onclick = "abrir_modal_eliminacion(\'/Base/eliminar_tipo/' + response[i]['pk'] +'/\');"> ELIMINAR </buttton></td>';
                fila += '</tr>';

                $('#tabla_tipos tbody').append(fila);
            }
            $('#tabla_tipos').DataTable({
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
	activarBoton();
    var data = new FormData($('#form_creacion').get(0));
    
    $.ajax({
        data: data,
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        cache:false,
        contentType:false,
        processData:false,
		success: function(response){
			notificacionSuccess(response.mensaje);
			listadoTipo();
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
            listadoTipo();
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
        url: '/Base/eliminar_tipo/'+pk+'/',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoTipo();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}
$(document).ready(function (){
    listadoTipo();
});