from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core import validators
from common.models import BaseModel

# Create your models here.


class User(AbstractBaseUser, BaseModel):

    # authentification attributes

    username = models.CharField(help_text='A unique name used to login to the system.',
            max_length=255, unique=True,
            validators=[validators.RegexValidator(r'^ [\w.@+-] +$',
                 'Enter a valid username, which means less than'
                '30 characters consisting of letters, numbers, '
                'or these symbols: @ +-_.',
                 'invalid'), ],
            error_messages={'unique': "Sorry, that username is already in use."})

    email = models.EmailField(help_text='A unique and valid email address.',
        unique=True,
        error_messages={'unique': "Sorry, that email is already in use."})



    #profile attributes

    first_name = models.CharField(max_length=30, blank=True, null=True)

    last_name  = models.CharField(max_length=30, blank=True, null=True)  
    
