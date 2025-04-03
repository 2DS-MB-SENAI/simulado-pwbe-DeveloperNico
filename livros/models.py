from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    paginas = models.IntegerField()

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = 'Livros'