# Generated by Django 4.2.4 on 2023-08-31 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='purchasing_price',
            field=models.FloatField(blank=True, default=0, max_length=950, null=True),
        ),
    ]