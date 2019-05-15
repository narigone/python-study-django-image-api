from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField('Nome', max_length=500, blank=True, null=True)
    image_file = models.FileField('Imagem', upload_to='../media/images', max_length=500)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

    def __str__(self):
        return self.name