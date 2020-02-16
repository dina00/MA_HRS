from django.contrib import admin
from employee.models import Employee, JobRoll, Department, Position, Allowance

# Register your models here.
admin.site.register(Employee)
admin.site.register(JobRoll)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Allowance)
