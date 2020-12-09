var $ = jQuery.noConflict();
function ListaTipo(){
    $.ajax({
        url:"/",
        type:"get",
        dataType:"json",
        cache:false,
        contentType:false,
        processData:false,
        success: function(response){
            
            console.log(response);
            var contenedor = "";
            for(var i = 0;i < response.length;i++){
                
                contenedor += '<div class="portfolio-item">';            
                contenedor += '<a class="portfolio-link" data-toggle="modal" href="#portfolioModal1">';
                contenedor += '<div class="portfolio-hover">';
                contenedor += '<div class="portfolio-hover-content">';
                contenedor += '<i class="fas fa-plus fa-3x"></i>';
                contenedor += '</div></div>';
                contenedor += '<img class="img-fluid tamaño-img" src="/media/'+response[i]["fields"]['imagen']+'" alt=""/>';
                contenedor += '</a>';
                contenedor += '<div class="portfolio-caption">';
                contenedor += '<div class="portfolio-caption-heading">'+response[i]["fields"]['nombre']+'</div>';
                /*
                el botón a continuacion permite enviar la clave primaria de el tipo de cancha, 
                la envia a la funcion buscar_fecha ubicada en Home/js/buscar-fecha.js
                para que se cargue un formulario con calendario y hora
                */
                contenedor += '<button class="btn btn-primary" onclick = "seleccionar_deporte(\'/filtro-cancha/' + response[i]['pk']+'/\');">Seleccionar</button>';
                contenedor += '</div></div>';
            } 
                $('#contenedor-tipo').html(contenedor)  

        },
        error: function(error){
            console.log(error);
        }

    });
}

$(document).ready(function (){
    ListaTipo();
});