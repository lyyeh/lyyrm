# Generated by Django 4.1.dev20210928112014 on 2021-10-01 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webform', '0007_alter_associate_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='associate',
            name='lastmodifiedby',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]