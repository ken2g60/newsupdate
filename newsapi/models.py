from django.db import models
from django.utils.translation import ugettext_lazy as _


class NewsModel(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    image = models.ImageField(_("Image"), upload_to=None)
    category = models.CharField(_("Category"), max_length=50)
    content = models.TextField()
    publisher = models.CharField(_("Publisher"), max_length=50, null=True, blank=True)
    website = models.URLField(_("Website"), max_length=200, null=True, blank=True) 
    source = models.CharField(_("Source"), max_length=50, null=True, blank=True)
    label = models.CharField(_("Label"), max_length=50, null=True, blank=True)
    country = models.CharField(_("Country"), max_length=50)
    created_at = models.DateTimeField(_("Create At"), auto_now_add=True)
    
    
class Location(models.Model):
    location = models.ForeignKey(NewsModel, related_name='location', on_delete=models.CASCADE)
    longtitude = models.FloatField(_("Longtitude"))
    latitude = models.FloatField(_("Latitude"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)