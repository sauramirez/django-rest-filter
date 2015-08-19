from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class RESTFrameworkModel(models.Model):
    """
    Base for test models that sets app_label, so they play nicely.
    """

    class Meta:
        app_label = 'tests'
        abstract = True


class BasicModel(RESTFrameworkModel):
    text = models.CharField(
        max_length=100,
        verbose_name=_("Text comes here"),
        help_text=_("Text description.")
    )
