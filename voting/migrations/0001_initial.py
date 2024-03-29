# Generated by Django 5.0.1 on 2024-01-26 16:02

import django.db.models.deletion
import voting.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('max_vote', models.IntegerField()),
                ('representative', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voters_file', models.FileField(upload_to='voters', validators=[voting.models.validate_voter_file])),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100, unique=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.college')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('scope', models.TextField(choices=[('1', 'University'), ('2', 'College'), ('3', 'Program')])),
                ('started', models.BooleanField(default=False)),
                ('year_level_limit', models.IntegerField(blank=True, choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')], null=True)),
                ('college_limit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.college')),
                ('course_limit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.course')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=50)),
                ('year_level', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')])),
                ('voted', models.BooleanField(default=False)),
                ('is_logged_in', models.BooleanField(default=False)),
                ('id_number', models.CharField(max_length=20)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.course')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='candidates')),
                ('bio', models.TextField()),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.election')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.position')),
                ('fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.voter')),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.candidate')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.position')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.voter')),
            ],
        ),
    ]
