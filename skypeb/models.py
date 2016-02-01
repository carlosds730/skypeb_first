from django.db import models


# Create your models here.

class Newsletter_Clients(models.Model):
    class Meta:
        verbose_name = 'Cliente de noticias'
        verbose_name_plural = 'Clientes de noticias'

    email = models.EmailField(verbose_name='Email', unique=True, help_text='Email al que mandar las noticias')

    def __str__(self):
        return str(self.email)
