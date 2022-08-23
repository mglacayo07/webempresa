from django.urls import path
from . import views

urlpatterns = [
    path('store/',views.store,name="store"),
    path('about/',views.about,name="about"),
    path('',views.home,name="home"),
]
