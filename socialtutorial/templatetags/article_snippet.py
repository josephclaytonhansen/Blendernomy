import re
from django.utils.html import strip_tags
from django import template
register = template.Library()

@register.simple_tag
def make_snippet(html):
    text_only = re.sub('[ \t]+', ' ', strip_tags(html))
    working = text_only.replace('\n ', '\n').strip()[:160]
    if working.endswith("."):
        return working + ".. <em style = 'color:var(--main-text-light);padding-left:.5rem;'>read more</em>"
    else:
        return working + "... <em style = 'color:var(--main-text-light);padding-left:.5rem;'>read more</em>"
