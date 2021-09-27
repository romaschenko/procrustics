from django import template

from analytics.models import Market

register = template.Library()


@register.simple_tag()
def get_markets():
    return Market.objects.all()

