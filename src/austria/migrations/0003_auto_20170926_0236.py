# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0002_auto_20170917_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eligible_voters', models.IntegerField(default=-1, null=True)),
                ('votes', models.IntegerField(default=-1)),
                ('valid', models.IntegerField(default=-1)),
                ('invalid', models.IntegerField(default=-1)),
                ('ts_result', models.DateTimeField(verbose_name='timestamp of bmi result')),
                ('district', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='viz.District')),
                ('election', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='viz.Election')),
            ],
            options={
                'get_latest_by': 'ts_result',
                'verbose_name': 'district result',
                'ordering': ['id'],
                'verbose_name_plural': 'district results',
            },
        ),
        migrations.CreateModel(
            name='ListDistrictResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('votes', models.IntegerField(default=-1, null=True)),
                ('district_result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viz.DistrictResult')),
                ('election_list', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viz.List')),
            ],
            options={
                'verbose_name_plural': 'list district results',
                'verbose_name': 'list district result',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ListREDResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('votes', models.IntegerField(default=-1, null=True)),
                ('election_list', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viz.List')),
            ],
            options={
                'verbose_name_plural': 'list regional electoral district results',
                'verbose_name': 'list regional electoral district result',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ListStateResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('votes', models.IntegerField(default=-1, null=True)),
                ('election_list', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viz.List')),
            ],
            options={
                'verbose_name_plural': 'list state results',
                'verbose_name': 'list state result',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='REDResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eligible_voters', models.IntegerField(default=-1, null=True)),
                ('votes', models.IntegerField(default=-1)),
                ('valid', models.IntegerField(default=-1)),
                ('invalid', models.IntegerField(default=-1)),
                ('ts_result', models.DateTimeField(verbose_name='timestamp of bmi result')),
                ('election', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='viz.Election')),
                ('regional_electoral_district', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='viz.RegionalElectoralDistrict')),
            ],
            options={
                'get_latest_by': 'ts_result',
                'verbose_name': 'regional electoral district result',
                'ordering': ['id'],
                'verbose_name_plural': 'regional electoral district results',
            },
        ),
        migrations.CreateModel(
            name='StateResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eligible_voters', models.IntegerField(default=-1, null=True)),
                ('votes', models.IntegerField(default=-1)),
                ('valid', models.IntegerField(default=-1)),
                ('invalid', models.IntegerField(default=-1)),
                ('ts_result', models.DateTimeField(verbose_name='timestamp of bmi result')),
                ('election', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='viz.Election')),
                ('state', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='viz.State')),
            ],
            options={
                'get_latest_by': 'ts_result',
                'verbose_name': 'state result',
                'ordering': ['id'],
                'verbose_name_plural': 'state results',
            },
        ),
        migrations.AddField(
            model_name='liststateresult',
            name='state_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viz.StateResult'),
        ),
        migrations.AddField(
            model_name='listredresult',
            name='red_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='viz.REDResult'),
        ),
    ]