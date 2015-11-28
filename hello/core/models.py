#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import fields


class TimeStampedModel(models.Model):
    """
    提供“创建时间”和“更新时间”字段的基类。
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created = fields.AutoCreatedField(_('created'))
    modified = fields.AutoLastModifiedField(_('modified'))

    class Meta:
        abstract = True


class TimeFramedModel(models.Model):
    """
    提供“开始”和“结束”字段的基类。
    """
    start = models.DateTimeField(_('start'), null=True, blank=True)
    end = models.DateTimeField(_('end'), null=True, blank=True)

    class Meta:
        abstract = True


class SimpleModel(TimeStampedModel):

    name = models.CharField(max_length=100)
