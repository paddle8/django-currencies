# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0003_code_as_primary_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='is_prefix',
            field=models.BooleanField(default=True, help_text='determines if the curreny symbol should come before or after the numerical value', verbose_name='is_prefix'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='currency',
            name='subunits',
            field=models.PositiveIntegerField(default=100, help_text='the number of units needed to break this amount into its lowest denomination. (eg USD has 100 subunits, meaning there are 100 cents in 1 dollar)', verbose_name='subunits'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='currency',
            name='subunit_separator',
            field=models.CharField(default='.', help_text='the separator between full values and subunits (eg in USD the . between dollars and cents)', max_length=2, verbose_name='subunit_separator'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='currency',
            name='thousands_separator',
            field=models.CharField(default=',', help_text='the separator between thousands in a number (eg in USD the , in 1,000)', max_length=1, verbose_name='thousands_separator'),
            preserve_default=True,
        ),
    ]
