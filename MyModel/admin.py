from django.contrib import admin
from models import Doctor
from models import Patient
from models import FamilyMember

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
	list_display = ('id' ,'uname' ,'password','doctor')

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('id' , 'uname' ,'password')

admin.site.register(Patient,PatientAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(FamilyMember)