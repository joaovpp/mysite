from django.db import models
from django.contrib.auth.models import User

STATUS = {
    (0, "Draft"),
    (1, "Publish")
}

class Post(models.Model):
    '''Classe herdada da classe Models do Django'''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    objects = models.Manager()

    class Meta:
        """Forma com que vai ordenar os objetos será pela created_on declarado acima"""
        ordering= ["-created_on"] # O "-" antes diz para ser em ordem Decrescente, sem seria Crescente

    def __str__(self):
        return self.title
