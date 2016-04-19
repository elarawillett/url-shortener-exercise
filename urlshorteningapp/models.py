from __future__ import unicode_literals
from django.db import models

class ShortenedURL(models.Model) :
    urlKey = models.CharField(max_length=200, unique=True, verbose_name="URL Key")   
    fullUrl = models.TextField(verbose_name="Full URL")
    
    def clean_fullUrl(self) :
        fullUrlInput = self.cleaned_data['fullUrl']
        
        #add http:// if no supported protocol in input
        if(not re.search(r'(f|ht)tps?://',fullUrlInput)) :
            fullUrlInput = "http://" + fullUrlInput
        
        #throw ValidationError if input still doesn't look like a URL
        val = URLValidator()
        val(fullUrlInput)
        
        return fullUrlInput
    
    def __str__(self) :
        return self.urlKey
