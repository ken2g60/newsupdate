from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from newsapi.models import NewsModel,  Location
from newsapi.api.serializers import NewsSerializer, LocationSerializer

class NewsAPIView(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request):
        news = NewsModel.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class LocationBasedNewsAPIView(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)
    


class LocationQueryAPIView(APIView):
    
    permission_classes = (AllowAny,)
    
    def get(self, request):
        country = self.request.query_params.get('country')
        location = NewsModel.objects.filter(country=country)
        serializer = NewsSerializer(location, many=True)
        return Response(serializer.data)