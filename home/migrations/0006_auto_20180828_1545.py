# Generated by Django 2.0.7 on 2018-08-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180826_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
