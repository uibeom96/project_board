# Generated by Django 3.1.5 on 2021-01-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20210105_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
    ]
