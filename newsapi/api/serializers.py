from rest_framework import serializers
from newsapi.models import NewsModel, Location


class LocationSerializer(serializers.Serializer):
    longtitude = serializers.FloatField()
    latitude = serializers.FloatField()
    
    class Meta:
        model = Location
        fields = ('longtitude', 'latitude', 'created_at')
        
        

class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    location = LocationSerializer(many=True)
    image = serializers.ImageField(required=False)
    category = serializers.CharField()
    content = serializers.CharField()
    publisher = serializers.CharField()
    website = serializers.CharField()
    source = serializers.CharField()
    label = serializers.CharField()
    country = serializers.CharField()
    created_at = serializers.CharField()
    
    
    class Meta:
        model = NewsModel
        fields = ('title', 'image', 'location', 'category', 'content', 'location', 'publisher', 'website', 'source', 'label', 'country', 'created_at')