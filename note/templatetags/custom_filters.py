from django import template
  
register = template.Library()
  
@register.filter()
def myswapcase(value):
    return value.swapcase()

@register.filter()
def title_filter(value):
    ls = value.split()
    return "_".join(ls)

@register.simple_tag
def simple_tag(value):
    return value.upper()