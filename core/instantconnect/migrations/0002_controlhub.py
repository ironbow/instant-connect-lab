# Generated by Django 4.1.4 on 2023-12-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instantconnect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlHub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bot_token', models.CharField(max_length=300)),
            ],
        ),
    ]
