# Generated by Django 2.1.2 on 2018-10-27 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20181027_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to='pages/profile_photos/'),
        ),
    ]
