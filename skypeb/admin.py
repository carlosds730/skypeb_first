from django.contrib import admin
from skypeb import models


# Register your models here.

class KeyWord(admin.ModelAdmin):
    model = models.KeyWord


class Des(admin.ModelAdmin):
    model = models.Description


class Cliente(admin.ModelAdmin):
    model = models.Newsletter_Clients


admin.site.register(models.KeyWord, KeyWord)
admin.site.register(models.Description, Des)
admin.site.register(models.Newsletter_Clients, Cliente)
