# Generated by Django 4.0.2 on 2022-03-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialtutorial', '0010_featuredvideo_rename_sheepframes_sheepframe'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=256)),
                ('display', models.CharField(blank=True, default='', max_length=256)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
    ]
