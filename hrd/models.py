from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    reports_to = models.IntegerField(null=True)
    emp_code = models.IntegerField(null=True)
    comp_id = models.IntegerField(null=True)
    dept_id = models.IntegerField(null=True)
    desg_id = models.IntegerField(null=True)
    grade_id = models.IntegerField(null=True)
    emp_name = models.CharField(max_length=255,null=True)
    emp_img = models.ImageField(upload_to='images/',null=True)
    emp_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    emp_dob = models.DateField(null=True)
    curr_addr = models.TextField(null=True)
    perm_addr = models.TextField(null=True)
    blood_grp = models.CharField(max_length=5,null=True)
    contact = models.CharField(max_length=15,null=True)

    alt_contact = models.CharField(max_length=15,null=True)
    email = models.CharField(max_length=30,null=True)
    driv_lic = models.CharField(max_length=255,null=True)
    aadhar_no = models.CharField(max_length=25,null=True)
    voter_id = models.CharField(max_length=50,null=True)
    pan_no = models.CharField(max_length=50,null=True)
    emp_type = models.IntegerField(null=True)
    emp_status = models.IntegerField(null=True)
    old_uan = models.CharField(max_length=50,null=True)
    curr_uan = models.CharField(max_length=50,null=True)
    old_pf = models.CharField(max_length=50,null=True)
    curr_pf = models.CharField(max_length=50,null=True)
    old_esi = models.CharField(max_length=50,null=True)
    curr_esi = models.CharField(max_length=50,null=True)
    join_dt = models.DateField(null=True)
    leave_dt = models.DateField(null=True)
    active = models.IntegerField(null=True)
    leave_allotted = models.IntegerField(null=True)
    deleted_at = models.DateTimeField(null=True)

class ComapnyMast(models.Model):
    name= models.CharField(max_length=50,null=True)
    description= models.TextField(null=True)

class DesigMast(models.Model):
    name= models.CharField(max_length=50,null=True)
    description= models.TextField(null=True)

class GradesMast(models.Model):
    name= models.CharField(max_length=50,null=True)
    description= models.TextField(null=True)

class StatusMast(models.Model):
    name= models.CharField(max_length=50,null=True)
    description= models.TextField(null=True)

class TypesMast(models.Model):
    name= models.CharField(max_length=50,null=True)
    description= models.TextField(null=True)

class AcademicsMast(models.Model):
    doman_of_study= models.CharField(max_length=50,null=True)
    emp_id= models.IntegerField(null=True)
    name_of_board= models.CharField(max_length=50,null=True)
    complete_in = models.DateField(null=True)  
    gared   = models.CharField(max_length=10,null=True)     
    document = models.FileField(upload_to='acedmic/',null=True)     
    note = models.TextField(max_length=255,null=True)     

class Experience(models.Model):
    company_name = models.CharField(max_length=255,null=True)
    job_type = models.CharField(max_length=255,null=True)
    designation = models.CharField(max_length=255,null=True)
    monthly_ctc = models.FloatField(null=True)
    comp_loc = models.CharField(max_length=255,null=True)
    comp_email = models.CharField(max_length=255,null=True)
    comp_doc = models.CharField(max_length=255,null=True)
    join_date = models.DateField(null=True)
    leave_date = models.DateField(null=True)

class BankDetails(models.Model):
    accou_hol_name = models.CharField(max_length=255,null=True)
    emp_id = models.IntegerField(null=True)
    accou_num = models.CharField(max_length=255,null=True)
    bank_name = models.CharField(max_length=255,null=True)
    ifsc_code = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    document = models.ImageField(upload_to='bankdoc/',null=True)
    note = models.TextField(max_length=255,null=True)    

class Document(models.Model):
    STATUS_CHOICES = (
        ('Provided', 'Provided'),
        ('Submitted', 'Submitted'),
    )
    emp_id = models.IntegerField(null=True)
    document_title = models.CharField(max_length=255,null=True)
    document_status = models.CharField(max_length=55,choices=STATUS_CHOICES,null=True)
    note = models.TextField(null=True)
    files = models.ImageField(upload_to='otherdocs/',null=True)
