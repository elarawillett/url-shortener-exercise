from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import ShortenedURL
from .forms import URLShorteningForm

#Redirect already shortened URLs to their full URLs
def redirect_page(request,short) :
    shortenedURL = get_object_or_404(ShortenedURL, urlKey=short)
    return redirect(shortenedURL.fullUrl)

#Create new shortened URLs
def home(request) :
    domain = request.META['HTTP_HOST']
    
    if(request.method=="POST") :
        form = URLShorteningForm(request.POST)
        if(form.is_valid()) :
            newShortenedURL = form.save()
            return render(request, 'urlshorteningapp/success.html',{'key':newShortenedURL.urlKey, 'domain':domain})
    else :
        form = URLShorteningForm()
    
    return render(request, 'urlshorteningapp/home.html', {'form':form, 'domain':domain})

