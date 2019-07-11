from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.filter
def lower(value):
    return value.lower()

@register.filter(name='getname')
def get_name(value):
    qs = value.split('/')[-3]
    return qs