
from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='phone_number')
@stringfilter
def phone_number(value: str):
    copy_val = value[:]
    if copy_val.startswith('+'):
        copy_val = copy_val[1:]
    formatted = '{} {} {} {}'.format(
        copy_val[:3], copy_val[3:6], copy_val[6:9], copy_val[9:]
    )
    return formatted
