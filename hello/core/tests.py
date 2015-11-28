from django.test import TestCase


from . import models


# Create your tests here.

class DateTimeTestCase(TestCase):
    def test_create(self):
        #print "DateTimeTestCase!"
        models.SimpleModel.objects.create(name="tommy")
        simple = models.SimpleModel()
        simple.name = "johnny"
        simple.save()

        from django.db import connection
        print connection.queries