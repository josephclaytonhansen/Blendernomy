# Generated by Django 4.0.2 on 2022-03-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialtutorial', '0004_productkey_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='productkey',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]