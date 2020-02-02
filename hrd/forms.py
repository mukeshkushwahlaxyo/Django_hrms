from django.contrib.auth.forms import UserCreationForm
from hrd.models import Employee,AcademicsMast,BankDetails,Document
from django.forms import ModelForm
from django import forms    

class PersonalInfo(ModelForm):
    blood_grp = forms.CharField(required=False)
    email = forms.CharField(required=False)
    alt_contact = forms.CharField(required=False)
    curr_addr = forms.CharField(required=False)

    class Meta(ModelForm):
        model = Employee
        fields = ('emp_name','emp_gender','emp_dob','blood_grp','contact','alt_contact','email','curr_addr','perm_addr')
        labels = {
             'emp_name':'Name',
             'emp_gender':'Gender',
             'emp_dob' :'Date of Birth',
             'blood_grp':'Blood Group',
             'contact':'Contact Number',
             'alt_contact':'Alternate Contact Number',
             'email':'Email',
             'curr_addr':'Current Residence',
             'perm_addr':'Permanent Residence',
         }

class OfficeInfo(ModelForm):
    class Meta(ModelForm):
        model = Employee
        fields = ('comp_id','dept_id','emp_type','emp_status','join_dt','leave_dt','emp_code','desg_id','reports_to')
        labels = {
             'comp_id':'Company Name',
             'dept_id':'Department',
             'emp_type' :'Employee Type',
             'emp_status':'Employee Status',
             'join_dt':'Joinning Date',
             'leave_dt':'Leave Date',
             'emp_code':'Employee Code',
             'desg_id':'Designation',
             'reports_to':'Reports To',
         } 
class AcademicsInfo(ModelForm):
    document = forms.CharField(required=False)
    note = forms.CharField(required=False)
    emp_id = forms.CharField(required=False)
    class Meta(ModelForm):
        model = AcademicsMast
        fields = ('doman_of_study','name_of_board','complete_in','gared','document','note','emp_id')
        labels = {
             'doman_of_study':'Domain Of Study',
             'name_of_board':'Name Of Board',
             'complete_in' :'Complete In',
             'gared':'Gared',
             'document':'Document',    
             'note':'Note',
             } 

class BankInfo(ModelForm):
    document = forms.CharField(required=False)
    note = forms.CharField(required=False)
    emp_id = forms.IntegerField(required=False)
    class Meta(ModelForm):
        model = BankDetails
        fields =('accou_hol_name','accou_num','bank_name','ifsc_code','branch','document','note','emp_id')
        labels={
            'accou_hol_name':'Account Holder Name',
            'accou_num':'Account Number',
            'bank_name':'Bank Name',
            'ifsc_code':'IFSC Code',
            'branch':'Branch',
            'document':'Document',
            'note':'Note',
        }

class Documents(ModelForm):
    class Meta(ModelForm):
        emp_id = forms.CharField(required=False)
        model  = Document
        fields = ('document_title','document_status','note','files','emp_id')
        labels={
            'document_title':'Document Title',
            'document_status':'Document Status',
            'note':'Note',
            'files':'File',
        }        

