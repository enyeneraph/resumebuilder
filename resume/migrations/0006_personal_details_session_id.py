# Generated by Django 3.2.4 on 2021-08-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20210731_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_details',
            name='session_id',
            field=models.CharField(default='missed', max_length=32),
        ),
    ]
