# Generated by Django 5.0.1 on 2024-01-26 16:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voting', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectoralCommittee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssc', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('fullname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('scope', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.college')),
            ],
        ),
    ]
