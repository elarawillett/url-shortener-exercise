from __future__ import unicode_literals
from django.db import models

class ShortenedURL(models.Model) :
    urlKey = models.CharField(max_length=200, unique=True, verbose_name="URL Key")   
    fullUrl = models.TextField(verbose_name="Full URL")
    
    def __str__(self) :
        return self.urlKey
