# Generated by Django 2.1.5 on 2019-03-20 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carparkData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('spaces', models.CharField(max_length=10, null=True)),
                ('area', models.CharField(max_length=50)),
                ('Timestamp', models.DateTimeField(null=True, verbose_name='date published')),
                ('cm_last_insert_dttm', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('roadname', models.CharField(max_length=100)),
                ('noofspaces', models.IntegerField()),
                ('spacetype', models.CharField(max_length=100)),
                ('OBJECTID', models.IntegerField()),
                ('Point', models.CharField(max_length=100)),
                ('lat', models.DecimalField(decimal_places=9, max_digits=12)),
                ('long', models.DecimalField(decimal_places=9, max_digits=12)),
                ('last_update', models.DateTimeField(null=True, verbose_name='date published')),
                ('cm_last_insert_dttm', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
