# Generated by Django 4.0.2 on 2022-03-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialtutorial', '0006_alter_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='SheepFrames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frames', models.IntegerField()),
            ],
        ),
    ]