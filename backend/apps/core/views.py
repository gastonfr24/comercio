from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def health_check(request):
    """
    Endpoint simple para verificar que la API está funcionando
    """
    return Response({
        'status': 'ok',
        'message': 'API funcionando correctamente'
    }, status=status.HTTP_200_OK)

