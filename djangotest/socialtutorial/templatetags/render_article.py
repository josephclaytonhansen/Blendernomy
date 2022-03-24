from django.utils.html import format_html
from django import template
register = template.Library()

@register.simple_tag
def render_article(val=None):
    return format_html(val)