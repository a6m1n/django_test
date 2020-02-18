"""Django custom template tags"""
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    """My custom tag which need to correct work django pagination and filter
    orders. Or update add to href query params.
    """
    query = context["request"].GET.copy()
    for key, value in kwargs.items():
        query[key] = value
    return query.urlencode()
