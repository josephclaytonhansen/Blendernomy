from django import template
register = template.Library()
from ..models import SheepFrame
from django.utils.html import format_html

@register.simple_tag
def get_frames():
  return str(SheepFrame.objects.all()[0].frames)
   
