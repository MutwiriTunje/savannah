# Generated by Django 5.1.1 on 2024-09-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
