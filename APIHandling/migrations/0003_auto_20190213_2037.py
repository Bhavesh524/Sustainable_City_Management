# Generated by Django 2.1.5 on 2019-02-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIHandling', '0002_auto_20190213_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='position_lnt',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bike',
            name='last_update',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]