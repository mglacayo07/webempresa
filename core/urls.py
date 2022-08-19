from django.urls import path
from . import views

urlpatterns = [
    path('sample/',views.home,name="sample"),
    path('contact/',views.contact,name="contact"),
    path('store/',views.store,name="store"),
    path('about/',views.about,name="about"),
    path('',views.home,name="home"),
]
