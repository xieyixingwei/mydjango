# Generated by Django 3.1.1 on 2021-02-04 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_uname', models.CharField(max_length=32, unique=True)),
                ('u_passwd', models.CharField(max_length=256)),
                ('u_is_admin', models.BooleanField(default=False)),
                ('u_register_date', models.DateTimeField(auto_now_add=True)),
                ('u_name', models.CharField(blank=True, max_length=32, null=True)),
                ('u_gender', models.BooleanField(null=True)),
                ('u_birthday', models.DateTimeField(null=True)),
                ('u_education', models.IntegerField(null=True)),
                ('u_wechart', models.CharField(max_length=64, null=True)),
                ('u_qq', models.CharField(max_length=64, null=True)),
                ('u_email', models.CharField(max_length=64, null=True)),
                ('u_telephone', models.CharField(max_length=16, null=True)),
                ('u_status', models.JSONField(null=True)),
            ],
        ),
    ]
