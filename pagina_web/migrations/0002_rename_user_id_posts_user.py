# Generated by Django 4.0.5 on 2022-07-13 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='user_id',
            new_name='user',
        ),
    ]