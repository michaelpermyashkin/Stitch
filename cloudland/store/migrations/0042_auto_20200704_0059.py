# Generated by Django 3.0.6 on 2020-07-04 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0041_auto_20200704_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description_short',
            field=models.CharField(default='', help_text='Limit 100 characters: Product description on item card', max_length=100),
        ),
    ]
