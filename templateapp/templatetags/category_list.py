from django import template
from ..models import CategoryModel

register = template.Library()

@register.simple_tag
def category_list():
    categories = CategoryModel.objects.all()
    return categories