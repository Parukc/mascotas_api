from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mascota
from .serializers import MascotaSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all().order_by('id')
    serializer_class = MascotaSerializer

    # Ensure all responses are JSON (DRF does this by default)

@api_view(['POST'])
def dosis_total(request):
    data = request.data
    dosis = data.get('dosisDiarias')
    if not isinstance(dosis, list):
        return Response({'error': 'dosisDiarias debe ser un arreglo de números'}, status=status.HTTP_400_BAD_REQUEST)
    total = 0
    for item in dosis:
        try:
            num = float(item)
        except (TypeError, ValueError):
            return Response({'error': 'Todos los elementos de dosisDiarias deben ser números'}, status=status.HTTP_400_BAD_REQUEST)
        total += num
    if total < 100:
        mensaje = 'Tratamiento de baja intensidad'
    elif 100 <= total <= 300:
        mensaje = 'Tratamiento moderado'
    else:
        mensaje = 'Tratamiento fuerte, seguir observación'
    return Response({'dosisTotal': total, 'mensaje': mensaje})

@api_view(['POST'])
def control_peso(request):
    data = request.data
    try:
        peso_actual = float(data.get('pesoActual'))
        peso_ideal = float(data.get('pesoIdeal'))
    except (TypeError, ValueError):
        return Response({'error': 'pesoActual y pesoIdeal deben ser números'}, status=status.HTTP_400_BAD_REQUEST)
    diferencia = peso_actual - peso_ideal
    if diferencia > 0:
        mensaje = 'La mascota está por encima del peso ideal'
    elif diferencia < 0:
        mensaje = 'La mascota está por debajo del peso ideal'
    else:
        mensaje = 'Peso ideal alcanzado'
    return Response({'diferencia': diferencia, 'mensaje': mensaje})
