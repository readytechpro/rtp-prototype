# Generated by Django 3.1.2 on 2021-03-12 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitecore', '0008_auto_20210311_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='label',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
