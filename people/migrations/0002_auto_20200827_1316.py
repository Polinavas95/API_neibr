# Generated by Django 3.1 on 2020-08-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbor',
            name='x_coord',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='neighbor',
            name='y_coord',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
