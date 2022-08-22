from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación",default=now)  # Fecha manual
    image = models.ImageField(upload_to='blog',verbose_name="Imagen", null=True, blank=True)  # Pude ser nuevo

    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)  # models.CASCADE eliminará en cascada cuando se borre el usuario

    categories = models.ManyToManyField(Category, verbose_name="Categorias")

    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")


    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ["-created"]

    def __str__(self):
        return self.title
