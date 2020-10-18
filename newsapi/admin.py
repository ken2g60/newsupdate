from django.contrib import admin
from .models import NewsModel, Location

    
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'category', 'content', 'created_at')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('longtitude', 'latitude', 'created_at')
    
       
admin.site.register(NewsModel, NewsAdmin)
admin.site.register(Location, LocationAdmin)