# Generated by Django 5.0.6 on 2024-06-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ratings',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
