# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 04:32
from __future__ import unicode_literals

from django.db import migrations, models
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_resume_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['sorting_value']},
        ),
        migrations.AlterModelOptions(
            name='line',
            options={'ordering': ['sorting_value']},
        ),
        migrations.AlterModelOptions(
            name='programmingskills',
            options={'ordering': ['sorting_value']},
        ),
        migrations.AlterModelOptions(
            name='workexperience',
            options={'ordering': ['sorting_value']},
        ),
        migrations.AddField(
            model_name='education',
            name='sorting_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='line',
            name='sorting_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='programmingskills',
            name='sorting_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='sorting_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='bullets',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='resume.Line'),
        ),
    ]
