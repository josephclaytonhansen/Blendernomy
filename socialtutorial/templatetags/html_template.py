from django import template
register = template.Library()

@register.simple_tag
def use_template(val=None):
  templates = {"undefined":"socialtutorial/csstemplates/null.css", "basic":"socialtutorial/csstemplates/basic.css"}
  active_template = templates[val]
  return active_template   
