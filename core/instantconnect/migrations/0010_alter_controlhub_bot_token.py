# Generated by Django 4.1.4 on 2023-12-01 23:45

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instantconnect', '0009_alter_controlhub_bot_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlhub',
            name='bot_token',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=300)),
        ),
    ]