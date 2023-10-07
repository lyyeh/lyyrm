from datetime import datetime

from django import forms
from django.forms import ModelForm
from .models import associate

from django.core.exceptions import ValidationError

class web_form(forms.Form):
    given_name = forms.CharField(label='Given Name', max_length=100)
    sur_name = forms.CharField(label='Sur Name', max_length=100)
    manager_id = forms.CharField(label='Manager\'s ID', max_length=10)
    contact_email = forms.CharField(label='Contact E-mail', max_length=100)
    start_date = forms.DateField(initial="12/30/1999",required=False)
    end_date = forms.DateField(initial="12/30/2000",required=False)
    job_code = forms.CharField(label='Job Code', max_length=32,required=False)
    workertype = forms.CharField(label='Worker Type', max_length=32,required=False)
    job_title = forms.CharField(label='Job Title', max_length=100,initial='Independent Contractor')
    supplier = forms.CharField(label='Supplier', max_length=100,initial='Independent')

       
class associate_form(ModelForm):
    class Meta:
        model = associate
        fields = ('givenname','surname','managerid','contactemail','hiredate','enddate','jobcode','petcoworkertype','petcojobtitle','supplier','petcolocation','petcolocationtype')
        labels = {
            'givenname': 'First name',
            'surname': 'Last name',
            'managerid': 'Manager\'s ID',
            'contactemail': 'Contact E-mail',
            'hiredate': 'Start date',
            'enddate': 'End date',
            'jobcode': 'Job Code',
            'petcoworkertype': 'Worker Type',
            'petcojobtitle': 'Job Title',
            'petcolocation': 'Location',
            'petcolocationtype': 'Location Type',
            'supplier': 'Agency',
        }
        widgets = {
            'givenname': forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name','required':'true'}),
            'surname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name','required':'true'}),
            'managerid': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Manager\'s ID','required':'true'}),
            'contactemail': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Contact E-mail : real@company.com','required':'true'}),
            'hiredate': forms.DateInput(attrs={'class': 'form-control','placeholder':'Start Date: 12/30/1999'}),
            'enddate': forms.DateInput(attrs={'class': 'form-control','placeholder':'End Date: 12/30/2000'}),
            'jobcode': forms.TextInput(attrs={'class': 'form-control','initial value': 'V1099'}),
            'petcoworkertype': forms.TextInput(attrs={'class': 'form-control','initial value': '1099'}),
            'petcojobtitle': forms.TextInput(attrs={'class': 'form-control','initial value': 'Independent Contractor'}),
            'petcolocation': forms.TextInput(attrs={'class': 'form-control','initial value': 'remote'}),
            'petcolocationtype': forms.TextInput(attrs={'class': 'form-control','initial value': 'remote'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control','initial value': 'Independent'}),
        }

class associate_detail(ModelForm):
    class Meta:
        model = associate
        fields = ('__all__')

        widgets = {
            'userid': forms.TextInput(attrs={'class': 'form-control' , 'required':'true'}),
            'displayname': forms.TextInput(attrs={'class': 'form-control', 'required':'true'}),
            'givenname': forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name','required':'true'}),
            'surname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}),
            'initials': forms.TextInput(attrs={'class': 'form-control'}),
            'petcocountry': forms.TextInput(attrs={'class': 'form-control'}),
            'managerid': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Manager\'s ID'}),
            'contactemail': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Contact E-mail : real@company.com'}),
            'hiredate': forms.DateInput(attrs={'class': 'form-control','placeholder':'Start Date: 12/30/1999'}),
            'enddate': forms.DateInput(attrs={'class': 'form-control','placeholder':'End Date: 12/30/2000'}),
            'jobcode': forms.TextInput(attrs={'class': 'form-control','initial value': 'V1099'}),
            'petcoworkertype': forms.TextInput(attrs={'class': 'form-control','initial value': '1099'}),
            'petcojobtitle': forms.TextInput(attrs={'class': 'form-control','initial value': 'Independent Contractor'}),
            'petcolocation': forms.TextInput(attrs={'class': 'form-control','initial value': 'remote'}),
            'petcolocationtype': forms.TextInput(attrs={'class': 'form-control','initial value': 'remote'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control','initial value': 'Independent'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'petcodepartment': forms.TextInput(attrs={'class': 'form-control'}),
            'petcocity': forms.TextInput(attrs={'class': 'form-control'}),
            'costcenter': forms.TextInput(attrs={'class': 'form-control'}),
            'petcopostalcode': forms.TextInput(attrs={'class': 'form-control'}),
            'petcostore': forms.TextInput(attrs={'class': 'form-control'}),
            'employeetype': forms.TextInput(attrs={'class': 'form-control'}),
            'petcodivision': forms.TextInput(attrs={'class': 'form-control'}),
            'petcodistrict': forms.TextInput(attrs={'class': 'form-control'}),
            'petcomarket': forms.TextInput(attrs={'class': 'form-control'}),
            'petcoterritory': forms.TextInput(attrs={'class': 'form-control'}),
            'petcodepartmentname': forms.TextInput(attrs={'class': 'form-control'}),
            'petcocompany': forms.TextInput(attrs={'class': 'form-control'}),
            'petcopaygroup': forms.TextInput(attrs={'class': 'form-control'}),
            'petcojobfamily': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_startdate': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_enddate': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.PasswordInput(attrs={'class': 'form-control'}),
            'requestnumber': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'lastmodifiedby': forms.TextInput(attrs={'class': 'form-control'}),
        }
        