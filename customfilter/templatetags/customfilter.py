#-*- coding: utf-8 -*-
from django import template
from datetime import date, timedelta
from ecolle.settings import NOM_ETABLISSEMENT

register = template.Library()

@register.filter
def nometab(d):
	return NOM_ETABLISSEMENT

@register.filter
def lookup(d,key):
    return d[key]

@register.filter
def integer(n):
    return int(n)

@register.filter
def addtime(temps, ajout):
    return temps+timedelta(days=ajout)

@register.filter
def heurecolle(nb,temps):
	return "{}h{:02d}".format(nb*temps//60,(nb*temps)%60)

@register.filter
def heure(heure):
	return "{}h{:02d}".format(heure//4,15*(heure%4))

@register.filter
def image(fichier):
    return fichier.replace('programme','image').replace('pdf','jpg')

@register.filter
def tzip(l1, l2):
    return zip(l1,l2)

