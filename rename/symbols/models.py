from django.db import models


SYMBOL_TYPES = (
    ('body_of_water','body_of_water'), 
    ('bridge','bridge'), 
    ('building','building'), 
    ('city','city'), 
    ('college','college'), 
    ('commemorative_license_plate','commemorative_license_plate'), 
    ('county','county'), 
    ('flag','flag'), 
    ('highway_or_roadway','highway_or_roadway'), 
    ('holiday_or_observances','holiday_or_observances'), 
    ('marker','marker'), 
    ('military_Base','military_Base'), 
    ('monument','monument'), 
    ('other','other'), 
    ('park','park'), 
    ('plaque','plaque'), 
    ('scholarship','scholarship'), 
    ('school','school'), 
    ('seal','seal'), 
    ('song','song'), 
)



# Create your models here.
class Symbol(models.Model): 
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    county = models.CharField(max_length=255)

    latitude = models.DecimalField(max_digits=11, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)

    symbol_type = models.CharField(max_length=30,choices=SYMBOL_TYPES)

    # contacts 
    # honorees 