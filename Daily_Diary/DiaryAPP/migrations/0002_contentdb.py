# Generated by Django 5.0 on 2023-12-30 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=10000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiaryAPP.dairy_db')),
            ],
        ),
    ]
