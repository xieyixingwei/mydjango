# Generated by Django 3.1.1 on 2021-02-03 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionary', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyWordTable',
            fields=[
                ('sw_id', models.AutoField(primary_key=True, serialize=False)),
                ('sw_collect', models.JSONField()),
                ('sw_familiarity', models.IntegerField()),
                ('sw_repeats', models.IntegerField()),
                ('sw_learn_record', models.JSONField()),
                ('sw_inplan', models.BooleanField()),
                ('sw_comments', models.CharField(max_length=256)),
                ('sw_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertable')),
                ('sw_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.wordtable')),
            ],
        ),
        migrations.CreateModel(
            name='StudySentenceTable',
            fields=[
                ('ss_id', models.AutoField(primary_key=True, serialize=False)),
                ('ss_collect', models.JSONField()),
                ('ss_familiarity', models.IntegerField()),
                ('ss_repeats', models.IntegerField()),
                ('ss_learn_record', models.JSONField()),
                ('ss_inplan', models.BooleanField()),
                ('ss_new_words', models.JSONField()),
                ('ss_next_sentences', models.JSONField()),
                ('ss_comments', models.CharField(max_length=256)),
                ('ss_sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.sentencetable')),
                ('ss_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='StudyPlanTable',
            fields=[
                ('sp_id', models.AutoField(primary_key=True, serialize=False)),
                ('sp_once_words', models.IntegerField()),
                ('sp_once_sentences', models.IntegerField()),
                ('sp_once_grammers', models.IntegerField()),
                ('sp_other_settings', models.JSONField()),
                ('sp_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='StudyGrammerTable',
            fields=[
                ('sg_id', models.AutoField(primary_key=True, serialize=False)),
                ('sg_familiarity', models.IntegerField()),
                ('sg_repeats', models.IntegerField()),
                ('sg_learn_record', models.JSONField()),
                ('sg_inplan', models.BooleanField()),
                ('sg_comments', models.CharField(max_length=256)),
                ('sg_grammer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.grammartable')),
                ('sg_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertable')),
            ],
        ),
    ]
