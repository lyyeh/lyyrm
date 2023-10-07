from django.db import models
from django.urls import reverse
from django.core import serializers

# Create your models here.

class associate(models.Model):
    userid = models.CharField(max_length=10, null=True, blank=True, unique=True)
    displayname = models.CharField(max_length=100, null=True, blank=True)
    givenname = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    initials = models.CharField(max_length=1, null=True, blank=True)
    petcocountry = models.CharField(max_length=100, null=True, blank=True)
    hiredate = models.DateField(max_length=10, null=True)
    enddate = models.DateField(max_length=10, null=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    petcodepartment = models.CharField(max_length=100, null=True, blank=True)
    petcocity = models.CharField(max_length=100, null=True, blank=True)
    costcenter = models.CharField(max_length=100, null=True, blank=True)
    petcopostalcode = models.CharField(max_length=100, null=True, blank=True)
    petcostore = models.CharField(max_length=100, null=True, blank=True)
    jobcode = models.CharField(max_length=100, null=True, blank=True)
    managerid = models.CharField(max_length=10, null=True)
    employeetype = models.CharField(max_length=100, null=True, blank=True)
    petcodivision = models.CharField(max_length=100, null=True, blank=True)
    petcodistrict = models.CharField(max_length=100, null=True, blank=True)
    petcomarket = models.CharField(max_length=100, null=True, blank=True)
    petcoterritory = models.CharField(max_length=100, null=True, blank=True)
    petcodepartmentname = models.CharField(max_length=100, null=True, blank=True)
    petcoworkertype = models.CharField(max_length=100, null=True, blank=True)
    petcojobtitle = models.CharField(max_length=100, null=True, blank=True)
    petcolocation = models.CharField(max_length=100, null=True, blank=True)
    petcolocationtype = models.CharField(max_length=100, null=True, blank=True)
    petcocompany = models.CharField(max_length=100, null=True, blank=True)
    petcopaygroup = models.CharField(max_length=100, null=True, blank=True)
    petcojobfamily = models.CharField(max_length=100, null=True, blank=True)
    contactemail = models.EmailField(max_length=100, unique=True)
    contract_startdate = models.DateField(max_length=10, null=True, blank=True)
    contract_enddate = models.DateField(max_length=10, null=True, blank=True)
    supplier = models.CharField(max_length=100, null=True, blank=True)
    pin = models.CharField(max_length=32, null=True, blank=True)
    lastmodifiedby = models.CharField(max_length=100, null=True, blank=True)
    requestnumber = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.userid) + ' | ' + str(self.contactemail)

    def get_absolute_url(self):
        return reverse('recorddetail',args=(str(self.id)))

# class RunnerSerializer(serializers.ModelSerializer):
    # https://docs.djangoproject.com/en/3.2/topics/serialization/
 #    progress = serializers.DecimalField(
 #       max_digits=5,
  #      decimal_places=2
 #   )
    
  #   def validate_progress(self, value):
  #      if not value:
 #           return value
 #       return value/100