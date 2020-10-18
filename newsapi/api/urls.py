from django.urls import path, include
from newsapi.api.views import NewsAPIView, LocationBasedNewsAPIView, LocationQueryAPIView

urlpatterns = [
    path('updates/', NewsAPIView.as_view()),
    path('location/', LocationBasedNewsAPIView.as_view()),
    path('location_query/<str:query>', LocationQueryAPIView.as_view()),
]