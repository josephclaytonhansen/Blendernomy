# Generated by Django 4.0.2 on 2022-03-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialtutorial', '0007_sheepframes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_on_home_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='featured_on_tag_page',
            field=models.BooleanField(default=False),
        ),
    ]
