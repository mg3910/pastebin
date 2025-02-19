from django.db import models
from enum import Enum
import random
import uuid
# Create your models here.


def rand_title():
    return str(hex(random.getrandbits(128))[2:])


class Language(models.TextChoices):
    Python = "Python"
    CPP    = "C++"
    C      = "C"
    JS     = "Javsacript"
    Java   = "Java"
    CSharp = "C#"
    Misc   = "Other"

class Paste(models.Model):
    #pid = models.AutoField(primary_key=True, unique=True)
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=128, default=rand_title)
    language = models.CharField(max_length=10, choices=Language.choices, 
                                default=Language.Misc)
    text = models.TextField()

    """
    def __str__(self):
        pass # LATER!

    """
    
