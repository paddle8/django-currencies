# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Currency = apps.get_model('currencies', 'currency')
    db_alias = schema_editor.connection.alias
    Currency.objects.using(db_alias).bulk_create([
        Currency(code='USD', name='US Dollar', symbol='$', is_active=True, is_default=True, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=','),
        Currency(code='EUR', name='Euro', symbol=u'\u20ac', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator=',', thousands_separator='.'),
        Currency(code='GBP', name='Pound Sterling', symbol=u'\u00a3', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=','),
        Currency(code='JPY', name='Japanese Yen', symbol=u'\u00a5', is_active=True, is_default=False, subunits=1, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=','),
        Currency(code='HKD', name='Hong Kong Dollar', symbol='HK$', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=','),
        Currency(code='CAD', name='Canadian Dollar', symbol='$', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=','),
        Currency(code='AUD', name='Australian Dollar', symbol='$', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=','),
        Currency(code='CHF', name='Swiss Franc', symbol='Fr.', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=False, subunit_separator='.', thousands_separator='\''),
        Currency(code='NOK', name='Norwegian Krone', symbol='kr', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=False, subunit_separator=',', thousands_separator='.'),
        Currency(code='CNY', name='Chinese Yuan', symbol=u'\u00a5', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=','),
        Currency(code='ZAR', name='South African Rand', symbol='R', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator=',', thousands_separator=' '),
        Currency(code='INR', name='Indian Rupee', symbol=u'\u20B9', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=','),
        Currency(code='BRL', name='Brazilian Real', symbol='R$', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator=',', thousands_separator='.'),
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Currency = apps.get_model('currencies', 'currency')
    db_alias = schema_editor.connection.alias
    Currency.objects.using(db_alias).filter(code='USD', name='US Dollar', symbol='$', is_active=True, is_default=True, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=',').delete()
    Currency.objects.using(db_alias).filter(code='EUR', name='Euro', symbol=u'\u20ac', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator=',', thousands_separator='.').delete()
    Currency.objects.using(db_alias).filter(code='GBP', name='Pound Sterling', symbol=u'\u00a3', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=',').delete()
    Currency.objects.using(db_alias).filter(code='JPY', name='Japanese Yen', symbol=u'\u00a5', is_active=True, is_default=False, subunits=1, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=',').delete()
    Currency.objects.using(db_alias).filter(code='HKD', name='Hong Kong Dollar', symbol='HK$', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=',').delete()
    Currency.objects.using(db_alias).filter(code='CAD', name='Canadian Dollar', symbol='$', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=',').delete()
    Currency.objects.using(db_alias).filter(code='AUD', name='Australian Dollar', symbol='$', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=',').delete()
    Currency.objects.using(db_alias).filter(code='CHF', name='Swiss Franc', symbol='Fr.', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=False, subunit_separator='.', thousands_separator='\'').delete()
    Currency.objects.using(db_alias).filter(code='NOK', name='Norwegian Krone', symbol='kr', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=False, subunit_separator=',', thousands_separator='.').delete()
    Currency.objects.using(db_alias).filter(code='CNY', name='Chinese Yuan', symbol=u'\u00a5', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=',').delete()
    Currency.objects.using(db_alias).filter(code='ZAR', name='South African Rand', symbol='R', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator=',', thousands_separator=' ').delete()
    Currency.objects.using(db_alias).filter(code='INR', name='Indian Rupee', symbol=u'\u20B9', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator='.', thousands_separator=',').delete()
    Currency.objects.using(db_alias).filter(code='BRL', name='Brazilian Real', symbol='R$', is_active=True, is_default=False, subunits=100, factor=1.000000, is_prefix=True, subunit_separator=',', thousands_separator='.').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0004_extra_fields'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
