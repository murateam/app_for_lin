# Generated by Django 2.1.5 on 2019-12-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user_avatars/%Y/%m/%d'),
        ),
    ]
