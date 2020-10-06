from django.db import models


# Create your models here.

class Department(models.Model):
    id = models.AutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=104
    )

    class Meta:
        db_table = 'department'
        managed = True


class Employee(models.Model):
    id = models.AutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=104
    )
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=True
    )

    class Meta:
        db_table = 'employee'
        managed = True
