# Generated by Django 3.1.1 on 2021-03-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0007_auto_20210311_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentencetable',
            old_name='paraphrase',
            new_name='paraphraseForeign',
        ),
    ]
