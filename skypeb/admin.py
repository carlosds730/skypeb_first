from django.contrib import admin
from skypeb import models


# Register your models here.

class KeyWord(admin.ModelAdmin):
    model = models.KeyWord


class Des(admin.ModelAdmin):
    model = models.Description


admin.site.register(models.KeyWord, KeyWord)
admin.site.register(models.Description, Des)
