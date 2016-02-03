from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, redirect, HttpResponse
from skypeb import models
from django.core.validators import validate_email
import json


def product_list(request):
    if request.is_ajax():
        try:
            mail = request.POST['mail']

            validate_email(mail)

            m, _ = models.Newsletter_Clients.objects.get_or_create(email=mail)
            m.save()
            return HttpResponse(json.dumps({'status': 1}), content_type='application/json')
        except KeyError:
            return HttpResponse(json.dumps({'status': 0}), content_type='application/json')
        except Exception as ee:
            return HttpResponse(json.dumps({'status': 0}), content_type='application/json')
    return render(request, 'index_1.html', {'keywords': models.KeyWord.objects.first().keyword,
                                            'description': models.Description.objects.first().description})


def google_thing(request):
    return render(request, 'google8d4d90f931ab89aa.html')
