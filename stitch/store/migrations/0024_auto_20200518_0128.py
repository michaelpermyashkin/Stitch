# Generated by Django 3.0.5 on 2020-05-18 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20200518_0103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]