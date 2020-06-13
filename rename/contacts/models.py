from django.db import models

# Create your models here.
class Contact(models.Model): 
	name=models.CharField(max_length=50)
	title=models.CharField(max_length=100)
	email=models.EmailField()
	phone_number=models.CharField(max_length=15)

	city=models.CharField(max_length=50)
	state=models.CharField(max_length=50)
	county=models.CharField(max_length=50)