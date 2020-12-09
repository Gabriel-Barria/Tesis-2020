from .models import Reserva

def mis_variables(request):
    reserva_false = Reserva.objects.filter(estado=False)
    return {'reserva_false': reserva_false}