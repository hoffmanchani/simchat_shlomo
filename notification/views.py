from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from notification import models
from django.conf import settings
import datetime
from django.core.mail import send_mail
import random

def index(request):
	print ('1111 email_list')
	families = models.Family.objects.all()
	for family in families:
		print ('email:', family.email)
	email_list = [family.email for family in families]
	context = {
		'families': [{'name':'bloyground', 'mobile':'999999999'}],
		'not_trim':random.randint(0,1000),
	}  
	msg_plain = loader.render_to_string('notification/notification_email.txt',context)
	msg_html =  loader.render_to_string('notification/notification_email.html',context)
	subject = 'hello, simchat shlomo'
	send_mail(subject, msg_plain, 'postmaster@sandbox03cad43ae8ee4e27bdabd4594722db43.mailgun.org',
				['hoffmanchani@gmail.com'],html_message=msg_html)
	print ('email list')
	template = loader.get_template('notification/index.html')

	return HttpResponse(template.render(context, request))


def register(request):
	betshemesh, _ = models.City.objects.get_or_create(name = 'Bet_shemesh')
	uria, _ = models.Street.objects.get_or_create(name = 'Uria', city = betshemesh)

	email_list = ['hoffmanchani@gmail.com', 'hoffmanchanisd2@gmail.com', 'hoffmanchanisd3@gmail.com']
	for email in email_list:
		models.Family.objects.get_or_create(email = email, street = uria)
	return HttpResponse('-------- family, wellcome! tizkoo lemitzvot!!!!!!!!!')



