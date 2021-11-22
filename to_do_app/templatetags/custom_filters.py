import re
from django import template

register = template.Library()


@register.filter(name = 'display_values')
def lower(value):
    value = re.sub('\w{1,}:', '', value)
    return value