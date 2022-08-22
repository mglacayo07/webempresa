from django.urls import path
from . import views


urlpatterns = [
    path('',views.blog,name="blog"),
    path('category/<int:category_id>/',views.category,name="category"),
    # siempre son cadenas los del path por eso debemos convertirlo a int
    # URL para más información:  https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters
]
