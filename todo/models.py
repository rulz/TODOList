# encoding: utf-8
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    """ 
    - Modelo Tarea, campos que son obligatorio para crear una tarea son:
        owner(ForeignKey) y name(CharField). 
    
    - campos opcionales:
        assigned_to(ForeignKey), description(TextField) y done(BooleanField).
    """

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
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __unicode__(self):
        return self.name
