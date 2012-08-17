# -*- coding: utf-8 -*-
from django import template
from django.forms.fields import ChoiceField

register = template.Library()


@register.filter
def field_display(field):
    """Returns the display value of a form field"""
    if isinstance(field.field, ChoiceField):
        for c in field.field.choices:
            if unicode(c[0]) == field.data:
                return c[1]
    else:
        return field.data
