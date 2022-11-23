from django.db import models
from django.contrib.auth.models import User


'''


class compoundCategory(models.Model):

    opi = 'opiates'
    htRec = 'ht-5 receptor agonists'
    canna = 'cannabinoids'


    comp_cat_choices  = [
        (opi, 'opiates'),
        (htRec, 'ht-5 receptor agonists'),
        (canna,'cannabinoids'),
        ]

'''


class docking_input(models.Model):
    #user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    title = models.CharField(primary_key=True, max_length=100, help_text='Enter an image title')
    pdb_file = models.FileField(null=True, blank=True, upload_to='images/')
    option1 = models.IntegerField(null=True)
    option2 = models.IntegerField(null=True)
    option3 = models.IntegerField(null=True)
    option4 = models.IntegerField(null=True)
    
