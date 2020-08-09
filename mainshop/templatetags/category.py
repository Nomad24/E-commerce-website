from django import template
from mainshop.models import Category

register = template.Library()


@register.inclusion_tag('mainshop/category_list.html')
def show_category():
    categories = Category.objects.all()
    return {"categories": categories}