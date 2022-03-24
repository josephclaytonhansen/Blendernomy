from django import template
register = template.Library()
from datetime import datetime

@register.simple_tag
def replace_date(val=None):
    final = str(val)
    return final
  
