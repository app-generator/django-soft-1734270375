# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    f_name = models.CharField(max_length=255, null=True, blank=True)
    f_address = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Order(models.Model):

    #__Order_FIELDS__
    f_char = models.CharField(max_length=255, null=True, blank=True)
    f_text = models.TextField(max_length=255, null=True, blank=True)
    f_bool = models.BooleanField()
    f_int = models.IntegerField(null=True, blank=True)

    #__Order_FIELDS__END

    class Meta:
        verbose_name        = _("Order")
        verbose_name_plural = _("Order")



#__MODELS__END
