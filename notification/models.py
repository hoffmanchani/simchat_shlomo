from django.db import models

class City(models.Model):
	name = models.CharField(max_length=200)

class Street(models.Model):
	name = models.CharField(max_length=200)
	neighborhood = models.CharField(max_length=200)
	city = models.ForeignKey(City, on_delete=models.CASCADE)


class Family(models.Model):
	email = models.CharField(max_length=200)
	street = models.ForeignKey(Street, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null = True)
	building = models.CharField(max_length=200, null = True)
	phone = models.CharField(max_length=200, null = True)
	mobile = models.CharField(max_length=200, null = True)
	def __str__(self):
		return self.name

class Host(models.Model):
	family = models.ForeignKey(Family, on_delete=models.CASCADE)
	guests_num = models.IntegerField(default=0)
	children_num = models.IntegerField(default=0)
	def __str__(self):
		return self.family

class Simcha(models.Model):
	family = models.ForeignKey(Family, on_delete=models.CASCADE)
	date = models.DateTimeField()
	appartment_num = models.IntegerField(default=0)
	def __str__(self):
		return self.family