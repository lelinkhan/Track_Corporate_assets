from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(blank=True, null=True)
    check_out_time = models.DateTimeField(default=timezone.now)
    check_in_condition = models.CharField(max_length=255, blank=True, null=True)
    check_out_condition = models.CharField(max_length=255)
