from django import template
register = template.Library()

@register.simple_tag
def get_keywords(val=None):
    article= val
    keywords = val.meta_keywords
    s = "blender,blender3d,blender tutorials,blender resources,blender3d tutorials,stylized art,blender texture painting, blender nodes, blender shaders, shader nodes, blender npr, blendernomy,"
    return s