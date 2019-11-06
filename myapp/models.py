# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ExperimentInfo(models.Model):
    exp_id = models.PositiveSmallIntegerField(primary_key=True)
    exp_magagername = models.CharField(max_length=12)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    exp_description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiment_info'


class SubsysInfo(models.Model):
    subsys_id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    description = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'subsys_info'


class VDataMonitor(models.Model):
    subsys_id = models.PositiveSmallIntegerField(primary_key=True)
    register_id = models.PositiveSmallIntegerField()
    exp_id = models.PositiveSmallIntegerField()
    v_data = models.FloatField()
    v_data_time = models.DateTimeField(auto_now_add=True)

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
    created_time = models.DateTimeField().auto_now_add
    created_manager = models.CharField(max_length=16)
    v_type = models.CharField(max_length=20)
    v_description = models.CharField(max_length=300)
    v_status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'v_info_register'
        unique_together = (('subsys_id', 'register_id'),)
    def get_Vname(self):
        return self.v_name