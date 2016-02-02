from django.db import models


# Create your models here.

class KeyWord(models.Model):
    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'

    keyword = models.TextField(verbose_name='keyword')


class Description(models.Model):
    class Meta:
        verbose_name = 'Description'
        verbose_name_plural = 'Descriptions'

    description = models.TextField(verbose_name='Description')


class Newsletter_Clients(models.Model):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    email = models.EmailField(verbose_name='Email', unique=True, help_text='Email al que mandar las cosas')

    def __str__(self):
        return str(self.email)
