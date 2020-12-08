var $ = jQuery.noConflict();
/*function mostrarErroresCreacion(errores){
    $('#errores').html("");
    let error = "";
    for (let item in errores.responseJSON.error){
        error += '<div class = "alert alert-danger"><strong>' + errores.responseJSON.error[item] + </strong></div>;

    }
    $('#errores').append(error);
}*/


jQuery(document).ready(function($) {

	"use strict";

	[].slice.call( document.querySelectorAll( 'select.cs-select' ) ).forEach( function(el) {
		new SelectFx(el);
	});

	jQuery('.selectpicker').selectpicker;


	

	$('.search-trigger').on('click', function(event) {
		event.preventDefault();
		event.stopPropagation();
		$('.search-trigger').parent('.header-left').addClass('open');
	});

	$('.search-close').on('click', function(event) {
		event.preventDefault();
		event.stopPropagation();
		$('.search-trigger').parent('.header-left').removeClass('open');
	});

	$('.equal-height').matchHeight({
		property: 'max-height'
	});

	// var chartsheight = $('.flotRealtime2').height();
	// $('.traffic-chart').css('height', chartsheight-122);


	// Counter Number
	$('.count').each(function () {
		$(this).prop('Counter',0).animate({
			Counter: $(this).text()
		}, {
			duration: 3000,
			easing: 'swing',
			step: function (now) {
				$(this).text(Math.ceil(now));
			}
		});
	});


	 
	 
	// Menu Trigger
	$('#menuToggle').on('click', function(event) {
		var windowWidth = $(window).width();   		 
		if (windowWidth<1010) { 
			$('body').removeClass('open'); 
			if (windowWidth<760){ 
				$('#left-panel').slideToggle(); 
			} else {
				$('#left-panel').toggleClass('open-menu');  
			} 
		} else {
			$('body').toggleClass('open');
			$('#left-panel').removeClass('open-menu');  
		} 
			 
	}); 

	 
	$(".menu-item-has-children.dropdown").each(function() {
		$(this).on('click', function() {
			var $temp_text = $(this).children('.dropdown-toggle').html();
			$(this).children('.sub-menu').prepend('<li class="subtitle">' + $temp_text + '</li>'); 
		});
	});


	// Load Resize 
	$(window).on("load resize", function(event) { 
		var windowWidth = $(window).width();  		 
		if (windowWidth<1010) {
			$('body').addClass('small-device'); 
		} else {
			$('body').removeClass('small-device');  
		} 
		
	});
  
 
});

function abrir_modal_edicion(url){    
    $('#edicion').load(url, function(){
      $(this).modal('show');
    });
  }
function abrir_modal_creacion(url){    
    $('#creacion').load(url, function(){
      $(this).modal('show');
    });
  }
  function abrir_modal_eliminacion(url) {
	$('#eliminacion').load(url, function () {
		$(this).modal('show');
	});
}
function cerrar_modal_creacion(){
	  $('#creacion').modal('hide');

  }
function cerrar_modal_edicion(){
	$('#edicion').modal('hide');
	
}
function cerrar_modal_eliminacion() {
	$('#eliminacion').modal('hide');
}
function activarBoton(){
	if($('#boton_creacion').prop('disabled')){
		$('#boton_creacion').prop('disabled',false);
	}else{
		$('#boton_creacion').prop('disabled',true);
	}

}
function mostrarErroresCreacion(errores){
	$('#errores').html("");
	let error = "";
	for(let item in errores.responseJSON.error){
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errores').append(error);
}
function mostrarErroresEdicion(errores) {
	$('#erroresEdicion').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#erroresEdicion').append(error);
}

function notificacionError(mensaje){
	Swal.fire({
		title: 'Error!',
		text: mensaje,
		icon: 'error'
	})
}

function notificacionSuccess(mensaje) {
	Swal.fire({
		title: 'Buen Trabajo!',
		text: mensaje,
		icon: 'success'
	})
}
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
	beforeSend: function(xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});



