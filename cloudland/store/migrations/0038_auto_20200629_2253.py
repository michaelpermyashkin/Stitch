# Generated by Django 3.0.6 on 2020-06-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_auto_20200629_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_featured',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(help_text='Hold down “Control”, or “Command” on a Mac, to select more than one.', to='store.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_short',
            field=models.CharField(default='', help_text='Limit 30 characters: Brief product description on item card', max_length=30),
        ),
    ]
