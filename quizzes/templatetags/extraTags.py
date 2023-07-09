from django import template

register = template.Library()

@register.filter
def getFromDict(dict, key):    
    return dict[key]