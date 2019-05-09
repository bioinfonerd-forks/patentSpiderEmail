import os
from email.header import make_header
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render
from patentSpider import settings


# Create your views here.
def send_email(request):
    email = EmailMessage('测试', 'test', settings.EMAIL_FROM, ['840212863@qq.com'])
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "resource", "Offline-tool.zip")
    file = open(file_path, 'rb').read()
    file_name = os.path.basename(file_path)
    b = make_header([(file_name, 'utf-8')]).encode('utf-8')
    email.attach(b, file)
    email.send()
    # send_mail('Subject here', 'Here is the message.', settings.EMAIL_FROM,
    #           ['840212863@qq.com'], fail_silently=False)
    return HttpResponse('ok')
