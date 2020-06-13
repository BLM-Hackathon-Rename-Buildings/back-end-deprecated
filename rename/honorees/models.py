from django.db import models


class Honoree(models.Model): 
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	photo = models.ImageField(null=True)