from django import template

register = template.Library()

@register.filter
def short(timesince):
    return timesince.split(',')[0]