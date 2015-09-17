# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class member_info(models.Model): #회원정보
    name = models.OneToOneField(User)
    realname = models.CharField(max_length=128)
    Tel = models.CharField(max_length=128)
    marry = models.CharField(max_length=128)

class money_info(models.Model): #년월 곗돈 현황
    name = models.ForeignKey(User)
    realname = models.CharField(max_length=128)
    year = models.CharField(max_length=128)
    month = models.CharField(max_length=128)
    ox = models.CharField(max_length=128)

class money_lost(models.Model): #미수금 현황
    name = models.ForeignKey(User)
    realname = models.CharField(max_length=128)
    lost_money = models.CharField(max_length=128)

class event(models.Model): #이벤트
    event_name = models.CharField(max_length=128)
    event_money = models.CharField(max_length=128)
    year = models.CharField(max_length=128)
    month = models.CharField(max_length=128)
    def __unicode__(self):
        return "%s"%(self.event_name,)

