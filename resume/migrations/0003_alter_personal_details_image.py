# Generated by Django 3.2.4 on 2021-07-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_personal_details_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
