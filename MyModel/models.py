# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    reg_no = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    hospital_address = models.CharField(max_length=255)
    hospital_name = models.CharField(max_length=255)
    home_address = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s %s %s ' % (self.doctor_id, self.uname, self.password)
    # class Meta:
    #     ##managed = False
    #     db_table = 'doctor'


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, blank=True, null=True)

    # class Meta:
    #     #managed = False
    #     db_table = 'patient'
    def __unicode__(self):
        return u'%s %s %s %s' % (self.patient_id, self.uname, self.password, self.doctor)


class FamilyMember(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)      
    patients = models.ManyToManyField(Patient,through='PatientFamily')

    # class Meta:
    #     #managed = False
    #     db_table = 'family_member'

class PatientFamily(models.Model):
    patient =models.ForeignKey(Patient)
    familymember = models.ForeignKey(FamilyMember)




# class PatientFamily(models.Model):
#     relationship_id = models.AutoField(primary_key=True)
#     patient = models.ForeignKey(Patient)
#     member = models.ForeignKey(FamilyMember)

#     class Meta:
#         managed = False
#         db_table = 'patient_family'

