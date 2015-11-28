#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.timezone import now


class AutoCreatedField(models.DateTimeField):
    """
    自动填充时间的日期时间类
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', now)
        super(AutoCreatedField, self).__init__(*args, **kwargs)


class AutoLastModifiedField(AutoCreatedField):
    """
    A DateTimeField that updates itself on each save() of the model.
    By default, sets editable=False and default=datetime.now.
    """

    def pre_save(self, model_instance, add):
        value = now()
        setattr(model_instance, self.attname, value)
        return value
