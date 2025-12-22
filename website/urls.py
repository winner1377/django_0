from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', index_view, name='home'),
    path('about',about_view, name= 'about'),
    path('contact',contact_view, name='contact'),
    path("test", test_views, name="test")
]
