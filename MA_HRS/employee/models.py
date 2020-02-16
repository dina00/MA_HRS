from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Employee (models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    ID_CHOICES =( ('S','State ID'), ('P', 'Passport'), ('D','Driving License'))
    STATUS_CHOICES = (('M','Married'),('D','Divorced'),('W','Widowed'),('S','Single'))
    MILITARY_CHOICES = (('E','EXEMPTED'),('P','POSTPONED'),('N','DOES NOT APPLY'),('A','ACTIVE'))
    RELIGION_CHOICES = (('M','MUSLIM'),('C','CHRISTIAN'),('J','JEWISH'),('O','OTHER'))

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100,unique=True)
    emp_number = models.PositiveIntegerField()
    address1 = models.CharField(max_length=264, blank=True, null=True)
    hire_date = models.DateField()
    phone_no = models.PositiveIntegerField()
    mobile_no = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField()
    identification_type = models.CharField(max_length=1, choices=ID_CHOICES)
    id_number = models.CharField(max_length=100,unique=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    field_of_study = models.CharField(max_length=100)
    education_degree = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    social_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    military_status = models.CharField(max_length=1, choices=MILITARY_CHOICES)
    religion = models.CharField(max_length=1, choices=RELIGION_CHOICES)
    insured = models.BooleanField()
    insurance_number= models.CharField(max_length=100, unique=True, blank=True)
    insurance_date = models.DateField()
    has_medical = models.BooleanField()
    medical_number = models.CharField(max_length=100, unique=True, blank=True)
    medical_date = models.DateField()
    created_by = models.ForeignKey('self', related_name='employee_created_by', on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateField()
    last_update_by = models.ForeignKey('self', related_name='employee_last_update_by', on_delete=models.CASCADE, blank=True, null=True)
    last_update_date = models.DateField()

    def __str__(self):
        full_name = self.first_name+' '+self.last_name
        return full_name



class JobRoll (models.Model):
    emp = models.ForeignKey(Employee, related_name='jobroll_emp',on_delete=models.CASCADE)
    manager = models.ForeignKey(Employee, related_name='jobroll_manager', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    job_name = models.CharField(max_length=100)
    created_by = models.ForeignKey('Employee', related_name='jobroll_created_by', on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateField()
    last_update_by = models.ForeignKey('Employee', related_name='jobroll_last_update_by', on_delete=models.CASCADE, blank=True, null=True)
    last_update_date = models.DateField()

    def __str__(self):
        return self.job_name


class Position (models.Model):
    dept = models.ForeignKey('Department', on_delete=models.CASCADE)
    position_name = models.CharField(max_length=100)
    position_description = models.CharField(max_length=264)
    created_by = models.ForeignKey('Employee', related_name='position_created_by', on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateField()
    last_update_by = models.ForeignKey('Employee', related_name='position_last_update_by', on_delete=models.CASCADE, blank=True, null=True)
    last_update_date = models.DateField()

    def __str__(self):
        return self.position_name

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    parent_dept = models.ForeignKey('self', related_name='parent_department', on_delete=models.CASCADE, blank=True, null=True)
    dept_type = models.CharField(max_length=100)
    created_by = models.ForeignKey('Employee', related_name='department_created_by', on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateField()
    last_update_by = models.ForeignKey('Employee', related_name='department_last_update_by', on_delete=models.CASCADE, blank=True, null=True)
    last_update_date = models.DateField()

    def __str__(self):
        return self.dept_name

class Allowance(models.Model):
    service_name = models.CharField(max_length=100)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    note = models.CharField(max_length=264, blank=True, null=True)
    attatchment = models.FileField(upload_to='documents/')
    calculation_type = models.CharField(max_length=100, blank=True, null=True)
    amount = models.PositiveIntegerField()
    type = models.CharField(max_length=100,blank=True, null=True)
    created_by = models.ForeignKey('Employee', related_name='allowance_created_by', on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateField()
    last_update_by = models.ForeignKey('Employee', related_name='allowance_last_update_by', on_delete=models.CASCADE, blank=True, null=True)
    last_update_date = models.DateField()

    def __str__(self):
        return self.service_name
