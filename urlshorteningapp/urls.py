from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^(?P<short>[a-zA-Z\d]+)/$', views.redirect_page, name='redirect_page'),
]