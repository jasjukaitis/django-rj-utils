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


@register.simple_tag
def mask_email_address(address):
    """Returns a spam bot safe email address."""
    address = address.replace('@', ' [at] ')
    address = address[::-1].replace('.', ' [dot] '[::-1], 1)
    return address[::-1]
