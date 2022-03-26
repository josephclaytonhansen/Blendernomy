from django import template
register = template.Library()

@register.simple_tag
def set_code_theme(val="None"):
  code_themes = {"Nebula":"socialtutorial/nebula.css", "Dark Violet":"socialtutorial/dark-violet.css", "Mocha":"socialtutorial/mocha.css", "Nord":"socialtutorial/nord.css"}
  active_theme = code_themes[val]
  return active_theme

