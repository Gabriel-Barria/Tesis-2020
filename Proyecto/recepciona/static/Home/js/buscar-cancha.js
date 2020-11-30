var $ = jQuery.noConflict();
function seleccionar_deporte(url){    
    $.ajax({
        url:url,
        type:"get",
        dataType:"json",
        cache:false,
        contentType:false,
        processData:false,
        success: function(response){
            $('#custom-content-below-profile-tab').click();
            var contenedor = "";
            console.log(response);
            for(var i = 0;i < response.length;i++){
                contenedor += '<div class="portfolio-item"><a class="portfolio-link" data-toggle="modal" href="#portfolioModal1"><div class="portfolio-hover"><div class="portfolio-hover-content"><i class="fas fa-plus fa-3x"></i></div></div><img class="img-fluid" src="/media/'+response[i]["fields"]['imagen']+'" alt=""/></a><div class="portfolio-caption"><div class="portfolio-caption-heading">'+response[i]["fields"]['nombre']+'</div><div class="portfolio-caption-subheading text-muted""><button class="btn btn-primary" onclick = "seleccionar_cancha(\'/mostrar-calendario/' + response[i]['pk']+'/\');">Seleccionar</button></div></div></div></div>';            
               } 
                $('#contenedor-cancha').html(contenedor)  

        },
        error: function(error){
            console.log(error);
        }

    });
   
  }
