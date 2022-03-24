from django import template
register = template.Library()

@register.simple_tag
def position(val=None):
    return val
