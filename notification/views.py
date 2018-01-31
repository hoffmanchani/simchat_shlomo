from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.http import HttpResponse
import requests
from notification import models


def index(request):
	print ('1111 email_list')
	email_list = []
	families = models.Family.objects.all()
	for family in families:
		print ('email:', family.email)


	print ('email list')
	requests.post(
	        "https://api.mailgun.net/v3/sandbox03cad43ae8ee4e27bdabd4594722db43.mailgun.org/messages",
	        auth=("api", "key-866d80251fcf9e55999583f1671e3496"),
	        data={"from": "Excited User <mailgun@sandbox03cad43ae8ee4e27bdabd4594722db43.mailgun.org>",
	              "to": ["hoffmanchanisd2@gmail.com", "hoffmanchani@gmail.com"],
	              "subject": "Hello",
	              "text": "Testing some Mailgun awesomness!"})
	print ('*****************email list')
	context = {
	'families': families,
	}
	template = loader.get_template('notification/index.html')

	return HttpResponse(template.render(context, request))


def register(request):
	betshemesh, _ = models.City.objects.get_or_create(name = 'Bet_shemesh')
	uria, _ = models.Street.objects.get_or_create(name = 'Uria', city = betshemesh)


	print ('register!!!!!')
	email ='levi@gmail.com'
	try:
		family = models.Family.objects.get(email = email)
	except models.Family.DoesNotExist:
		family = models.Family.objects.create(name = 'levi',
			street = uria,
			building = '1',
			phone = '029999999',
			mobile = '1111111111',
			email = 'asdasdfedfa@gmail.com',
			)
	return HttpResponse('levi family, wellcome! tizkoo lemitzvot!!!!!!!!!')



