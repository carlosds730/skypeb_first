from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, redirect, HttpResponse
from skypeb import models
from django.core.validators import validate_email
from django.core.mail import EmailMessage
import json


def product_list(request):
    if request.is_ajax():
        try:
            mail = request.POST['mail']

            validate_email(mail)

            m, _ = models.Newsletter_Clients.objects.get_or_create(email=mail)
            m.save()

            html_content = '<p>Hola, que genial eres y lo se porque te has inscrito en la mejor página, donde vas a poder comprar accesorios de móviles, tablets y ordenadores a precios increibles. </p><p>Solo por este voto de confianza depositado en nosotros, por tu tiempo y tu interés queremos dar las gracias.</p><p>En breve te avisamos para que seas de los primeros en comprar y recibir tu producto sentado en el sofa de casa viendo la tele...RING-RING....llegó el cartero!!! Y esta vez trae tu primer codigo de descuento para que lo utilices cuando esté lista nuestra página.</p><p><strong>Código descuento:</strong> WelcomeToTheFamily </p><p>Contamos con tu like, click aquí -> <a title="Like this on Facebook" href="https://www.facebook.com/SlimPeb-1514648538838924/"><img title="SlimPeb en Facebook"src="https://slimpeb.com/static/images/megusta.png" alt="" height="20" width="20" /></a></p><p>Avisa a tus amigos para que también tengan su código de descuento... :)</p>\n<p><a href="https://www.slimpeb.com">slimpeb.com</a></p>\n<p>PS:Si tienes cualquier duda (o simplemente estás aburrid@), escríbenos a <a href="mailto:slimpeb_info@towpeb.com">slimpeb_info@towpeb.com</a></p>'

            msg = EmailMessage(subject='Bienvenido a SlimPeb tu tienda de accesorios', body=html_content,
                               from_email='SlimPeb <no-reply@slimpeb.com>',
                               reply_to=['slimpeb_info@towpeb.com'],
                               to=[mail])
            msg.content_subtype = "html"  # Main content is now text/html

            msg.send()

            return HttpResponse(json.dumps({'status': 1}), content_type='application/json')
        except KeyError:
            return HttpResponse(json.dumps({'status': 0}), content_type='application/json')
        except Exception as ee:
            return HttpResponse(json.dumps({'status': 0}), content_type='application/json')
    return render(request, 'index.html', {'keywords': models.KeyWord.objects.first().keyword,
                                          'description': models.Description.objects.first().description})


def google_thing(request):
    return render(request, 'google8d4d90f931ab89aa.html')


def google_thing_1(request):
    return render(request, 'googleef2ef230e52b5386.html')
