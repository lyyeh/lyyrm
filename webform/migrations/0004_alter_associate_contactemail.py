# Generated by Django 4.1.dev20210928112014 on 2021-10-01 05:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webform', '0003_alter_associate_comment_alter_associate_contactemail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='contactemail',
            field=models.EmailField(blank=True, default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]