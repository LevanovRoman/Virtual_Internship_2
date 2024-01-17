from django.http import JsonResponse
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from .serializers import *


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class CoordinatesViewSet(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ('user__email', )

    # создание перевала
    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)

        # Результаты метода: JSON
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data['id'],
            })
        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad Request',
                'id': None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Ошибка подключения к базе данных',
                'id': None,
            })


class EmailAPIView(generics.ListAPIView):
    serializer_class = PerevalSerializer

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if Pereval.objects.filter(user__email=email):
            data = PerevalSerializer(Pereval.objects.filter(user__email=email), many=True).data
            api_status = status.HTTP_200_OK
        else:
            data = {
                'message': f'Не существует пользователя с таким email - {email}'
            }
            api_status = 404
        return JsonResponse(data, status=api_status, safe=False)