"""Django custom template tags"""
from django import template
from urllib.parse import urlencode

from django.template.context import RequestContext

register = template.Library()


@register.simple_tag(takes_context=True)
def query_transform(context: RequestContext, **kwargs) -> str:
    """My custom tag which need to correct work django pagination and filter
    orders. Or update add to href query params.
    """
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)
