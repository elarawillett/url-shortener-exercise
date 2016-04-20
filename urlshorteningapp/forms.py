from django import forms
from django.core.validators import URLValidator, ValidationError
from .models import ShortenedURL
import re

class URLShorteningForm(forms.ModelForm) :
    
    class Meta :
        model = ShortenedURL
        fields = ('fullUrl','urlKey')
        
    def clean_fullUrl(self) :
        fullUrlInput = self.cleaned_data['fullUrl']
    
        #add http:// if no supported protocol in input
        if(not re.search(r'(f|ht)tps?://',fullUrlInput)) :
            fullUrlInput = "http://" + fullUrlInput
        
        #throws ValidationError if input still doesn't look like a URL
        val = URLValidator()
        val(fullUrlInput)
            
        return fullUrlInput
    
    def clean_urlKey(self) :
        urlKeyInput = self.cleaned_data['urlKey']
           
        if(not re.match(r'^[a-zA-Z\d]+$',urlKeyInput)) :
            raise ValidationError("Sorry. Only letters and digits are allowed.")
        
        return urlKeyInput
        

        
    