# Generated by Django 4.1.dev20210928112014 on 2021-09-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='associates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('displayname', models.CharField(max_length=100)),
                ('givenname', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('initials', models.CharField(max_length=1)),
                ('petcocountry', models.CharField(max_length=100)),
                ('hiredate', models.DateField(max_length=10)),
                ('enddate', models.DateField(max_length=10)),
                ('status', models.CharField(max_length=100)),
                ('petcodepartment', models.CharField(max_length=100)),
                ('petcocity', models.CharField(max_length=100)),
                ('costcenter', models.CharField(max_length=100)),
                ('petcopostalcode', models.CharField(max_length=100)),
                ('petcostore', models.CharField(max_length=100)),
                ('jobcode', models.CharField(max_length=100)),
                ('managerid', models.CharField(max_length=10)),
                ('employeetype', models.CharField(max_length=100)),
                ('petcodivision', models.CharField(max_length=100)),
                ('petcodistrict', models.CharField(max_length=100)),
                ('petcomarket', models.CharField(max_length=100)),
                ('petcoterritory', models.CharField(max_length=100)),
                ('petcodepartmentname', models.CharField(max_length=100)),
                ('petcoworkertype', models.CharField(max_length=100)),
                ('petcojobtitle', models.CharField(max_length=100)),
                ('petcolocation', models.CharField(max_length=100)),
                ('petcolocationtype', models.CharField(max_length=100)),
                ('petcocompany', models.CharField(max_length=100)),
                ('petcopaygroup', models.CharField(max_length=100)),
                ('petcojobfamily', models.CharField(max_length=100)),
                ('contactemail', models.EmailField(max_length=100)),
                ('contract_startdate', models.DateField(max_length=10)),
                ('contract_enddate', models.DateField(max_length=10)),
                ('supplier', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=32)),
                ('requestnumber', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
    ]