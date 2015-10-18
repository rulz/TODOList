from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    owner = models.ForeignKey(
        'auth.User', verbose_name=_('Owner'), related_name='owners'
    )
    assigned_to = models.ForeignKey(
        'auth.User', verbose_name=_('Assigned to'),
        blank=True, null=True, related_name='assigneds'
    )
    name = models.CharField(
        max_length=50, verbose_name=_('Name')
    )
    description = models.TextField(
        verbose_name=_('Description'), blank=True
    )
    done = models.BooleanField(
        default=False, verbose_name=_('Done')
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_('Created')
    )
    modified = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_('Modified')
    )

    class Meta:
        verbose_name = _('Task list')
        verbose_name_plural = _('Task lists')

    def __unicode__(self):
        return self.name
