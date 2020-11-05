var $ = jQuery.noConflict();
function listadoCancha(){
    $.ajax({
        url:"/Base/Cancha/listar_cancha/",
        type:"get",
        dataType:"json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#tabla_canchas')){
                $('#tabla_canchas').DataTable().destroy();
            }
            console.log(response);
            $('#tabla_canchas tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i +1) + '</td>';
                fila += '<td>' + response[i]["fields"]['nombre'] + '</td>';
                fila += '<td>' + response[i]["fields"]['descripcion'] + '</td>';
                fila += '<td>' + response[i]["fields"]['valor'] + '</td>';
                fila += '<td>' + response[i]["fields"]['servicios'] + '</td>';
                fila += '<td>' + response[i]["fields"]['tipo_cancha'] + '</td>';
                fila += '<td>' + response[i]["fields"]['superficie'] + '</td>';
                fila += '<td>' + response[i]["fields"]['centro_dep'] + '</td>';
                fila += '<td><button> EDITAR </button><button>Eliminar</button></td>';
                fila += '</tr>';

                $('#tabla_canchas tbody').append(fila);
            }
            $('#tabla_canchas').DataTable({
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
			
			listadoCancha();
			cerrar_modal_creacion();
		},	
		error: function(error){
			console.log(error);
			
		}
	});
}

$(document).ready(function (){
    listadoCancha();
});