# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtImage',
            fields=[
                ('file_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='extended_app_extimage_file', serialize=False, to='filer.File')),
                ('_height', models.IntegerField(blank=True, null=True)),
                ('_width', models.IntegerField(blank=True, null=True)),
                ('default_alt_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='default alt text')),
                ('default_caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='default caption')),
                ('subject_location', models.CharField(blank=True, default='', max_length=64, verbose_name='subject location')),
            ],
            bases=('filer.file',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='filer.File')),
            ],
            bases=('filer.file',),
        ),
    ]