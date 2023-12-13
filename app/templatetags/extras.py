from django import template

register = template.Library()


@register.filter(name='neg')
def neg(value):
    return -value
