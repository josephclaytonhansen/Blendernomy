from django import template
register = template.Library()
from ..models import Banner
from django.utils.html import format_html

@register.simple_tag
def load_banner():
  if len(Banner.objects.all()) != 0:
    return format_html(Banner.objects.all().filter(published=True).order_by('id').reverse()[0].body)
  else:
        return format_html("")
   
