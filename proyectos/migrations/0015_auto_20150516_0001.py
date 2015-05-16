# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0014_auto_20150515_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date(2015, 5, 16), auto_now_add=True, help_text=b'Fecha de creacion del Proyecto', null=True),
            preserve_default=True,
        ),
    ]
