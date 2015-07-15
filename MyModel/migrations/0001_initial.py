# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
                ('reg_no', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('hospital_address', models.CharField(max_length=255)),
                ('hospital_name', models.CharField(max_length=255)),
                ('home_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('doctor', models.ForeignKey(blank=True, to='MyModel.Doctor', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientFamily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('familymember', models.ForeignKey(to='MyModel.FamilyMember')),
                ('patient', models.ForeignKey(to='MyModel.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='familymember',
            name='patients',
            field=models.ManyToManyField(to='MyModel.Patient', through='MyModel.PatientFamily'),
        ),
    ]
