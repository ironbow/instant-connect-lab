# Generated by Django 4.1.4 on 2023-12-01 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instantconnect', '0002_controlhub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='id',
        ),
        migrations.AddField(
            model_name='devices',
            name='control_hub',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='instantconnect.controlhub'),
            preserve_default=False,
        ),
    ]
