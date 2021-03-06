from django.template import Library
from urllib.parse import urlencode


register = Library()


@register.simple_tag
def query_string(*args, **kwargs):
    return urlencode(kwargs)
