from django.db import models
from enum import Enum
import random
# Create your models here.

def rand_title():
    return str(hex(random.getrandbits(128))[2:])

class Language(models.TextChoices):
    Python = "Python"
    CPP    = "C++"
    C      = "C"
    JS     = "Javsacript"
    Java   = "Java"
    CSHARP = "C#"
    MISC   = "Other"

class Paste(models.Model):
    #pid = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=128, default=rand_title)
    language = models.CharField(max_length=10, choices=Language.choices, 
                                default=Language.MISC)
    text = models.TextField()

    """
    def __str__(self):
        pass # LATER!

    """
    
