from django import template
register = template.Library()

@register.simple_tag
def increment(val=None):
    article= val
    article.views += 1
    article.save()
    return article.views
