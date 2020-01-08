# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class DataProcessIpc(models.Model):
    process_name = models.CharField(max_length=45)
    process_status = models.CharField(max_length=45, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_process_ipc'




class ExperimentInfo(models.Model):
    exp_id = models.PositiveSmallIntegerField(primary_key=True)
    exp_magagername = models.CharField(max_length=12)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    exp_description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiment_info'


class NisUserInfo(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nis_user_info'


class SubsysInfo(models.Model):
    subsys_id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    description = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'subsys_info'


class Test1(models.Model):
    num1 = models.IntegerField(blank=True, null=True)
    num2 = models.SmallIntegerField(blank=True, null=True)
    num3 = models.IntegerField(blank=True, null=True)
    num4 = models.IntegerField(blank=True, null=True)
    num5 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test1'


class VDataMonitor(models.Model):
    subsys_id = models.PositiveSmallIntegerField(primary_key=True)
    register_id = models.PositiveSmallIntegerField()
    exp_id = models.PositiveSmallIntegerField()
    v_data = models.FloatField()
    v_data_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'v_data_monitor'
        unique_together = (('subsys_id', 'register_id', 'exp_id', 'v_data_time'),)


class VFormonitoring(models.Model):
    subsys_id = models.PositiveSmallIntegerField(primary_key=True)
    register_id = models.PositiveSmallIntegerField()
    ip_port = models.CharField(max_length=100)
    v_register = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_formonitoring'
        unique_together = (('subsys_id', 'register_id'),)


class VInfoRegister(models.Model):
    subsys_id = models.PositiveSmallIntegerField(primary_key=True)
    register_id = models.PositiveSmallIntegerField()
    v_name = models.CharField(max_length=100)
    ip_port = models.CharField(max_length=100)
    created_time = models.DateTimeField()
    created_manager = models.CharField(max_length=16)
    v_type = models.CharField(max_length=20)
    v_description = models.CharField(max_length=300)
    v_status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'v_info_register'
        unique_together = (('subsys_id', 'register_id'),)
