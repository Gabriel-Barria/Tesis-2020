function cargar_calendario() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {

      select: function(selectionInfo) {                                
            $('#myModal').modal('show');
        },


      initialView: 'timeGridThreeDay',
      themeSystem: 'bootstrap',
      timeZone: 'UTC',
      editable: true,
      selectable: true,
      events: [
      
        
        
      ],
      views: {
        timeGridThreeDay: {
        type: 'timeGrid',
        duration: { days: 3 },
        
        }
      }
    });
    calendar.setOption('locale','Es')
    calendar.render();
   
  };

