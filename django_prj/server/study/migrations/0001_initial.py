# Generated by Django 3.1.1 on 2021-03-11 08:34

from django.db import migrations, models
import django.db.models.deletion
import server.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyWordTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('collect', server.models.JSONFieldUtf8()),
                ('familiarity', models.IntegerField()),
                ('repeats', models.IntegerField()),
                ('learnRecord', server.models.JSONFieldUtf8()),
                ('inplan', models.BooleanField()),
                ('comments', models.CharField(max_length=256)),
                ('foreignUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertable')),
                ('foreignWord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.wordtable')),
            ],
        ),
        migrations.CreateModel(
            name='StudySentenceTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('collect', server.models.JSONFieldUtf8()),
                ('familiarity', models.IntegerField()),
                ('repeats', models.IntegerField()),
                ('learnRecord', server.models.JSONFieldUtf8()),
                ('inplan', models.BooleanField()),
                ('newWords', server.models.JSONFieldUtf8()),
                ('nextSentences', server.models.JSONFieldUtf8()),
                ('comments', models.CharField(max_length=256)),
                ('foreignSentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.sentencetable')),
                ('foreignUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='StudyPlanTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('once_words', models.IntegerField()),
                ('onceSentences', models.IntegerField()),
                ('onceGrammers', models.IntegerField()),
                ('otherSettings', server.models.JSONFieldUtf8()),
                ('foreignUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='StudyGrammerTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('familiarity', models.IntegerField()),
                ('repeats', models.IntegerField()),
                ('learnRecord', server.models.JSONFieldUtf8()),
                ('inplan', models.BooleanField()),
                ('comments', models.CharField(max_length=256)),
                ('foreignGrammer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.grammartable')),
                ('foreignUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertable')),
            ],
        ),
    ]
