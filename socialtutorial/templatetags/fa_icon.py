from django import template
register = template.Library()
import ast

@register.simple_tag
def render_icon(val=None):
    val = ast.literal_eval(val)
    aria_label = val["label"]
    sid = val["id"]
    icon = val["icon"]
    click = val["click"]
    working = ['<div class = "icon-box t-icon-box"><i class="fa-solid ',
               ' fa-fw strong-icon t-icon t-icon-box"></i></div>']
    final = ['<div class = "t-panel" id = ',
             ' onclick = ',
             ' aria-label = "',
             '" data-balloon-pos="right">',
             '</div>']
    return final[0] + sid + final[1] + click + final[2] + aria_label + final[3] + working[0] + icon + working[1] + final[4]

