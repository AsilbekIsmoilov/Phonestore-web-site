from django import template
from store.models import Category, Like

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()

def get_filter():
    filters = [
        {
            "title":"Price",
            "filters":[
                ["-price","hight to low"],
                ["price","low to high"],
        ]
    },
        {
            "title": "Name",
            "filters": [
                ["-title", "A - Z"],
                ["title", "Z - A"],
            ]
        },
        {
            "title": "Color",
            "filters": [
                ["-color", "A - Z"],
                ["color", "Z - A"],
            ]
        }
    ]
    return filters


@register.simple_tag()
def get_like(user):
    likes = Like.objects.filter(user=user)
    products = [i.product for i in likes]
    return products
