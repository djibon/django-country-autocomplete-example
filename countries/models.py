from django.db import models

class Country(models.Model):
    """
    Country Model.
    """
    name = models.CharField(max_length=512)
    code = models.CharField(max_length=3)

    class Meta:
        ordering = ('code','name')

    def __unicode__(self):
        return self.name
    

class City(models.Model):
    """
    City Model.
    """
    country = models.ForeignKey(Country, blank=False, null=False)
    name = models.CharField(max_length=512)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.country.code)

