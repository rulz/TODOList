# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('done', models.BooleanField(default=False, verbose_name='Done')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('assigned_to', models.ForeignKey(related_name='assigneds', verbose_name='Assigned to', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(related_name='owners', verbose_name='Owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task list',
                'verbose_name_plural': 'Task lists',
            },
        ),
    ]
