# Generated by Django 3.0.6 on 2020-05-29 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_emailconfirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailconfirmed',
            old_name='hash_key',
            new_name='activations_key',
        ),
    ]