from django.db import models


# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        db_column='created_at',
        null=False,
        auto_now_add=True
    )
    modifed_at = models.DateTimeField(
        db_column='modified_at',
        null=False,
        auto_now=True
    )
    active = models.BooleanField(
        db_column='active',
        null=False,
        default=True
    )

    class Meta:
        abstract = True


# id, created_at, modified_at, active

class Department(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=104
    )

    class Meta:
        db_table = 'department'
        managed = True


class Employee(ModelBase):
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


class Category(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=104
    )
    comission_percentage = models.DecimalField(
        db_column='comission_percentage',
        null=False,
        max_digits=10,
        decimal_places=2
    )
    products = models.ManyToManyField(
        to='Product',
        through='ProductCategory'
    )

    class Meta:
        db_table = 'category'
        managed = True


class Product(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=104
    )
    price = models.DecimalField(
        db_column='price',
        null=False,
        max_digits=10,
        decimal_places=2
    )
    categories = models.ManyToManyField(
        to='Category',
        through='ProductCategory'
    )

    class Meta:
        db_table = 'product'
        managed = True


class ProductCategory(ModelBase):
    category = models.ForeignKey(
        to='Category',
        on_delete=models.DO_NOTHING,
        db_column='id_category',
        null=False
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False
    )

    class Meta:
        db_table = 'product_category'
        managed = True
        unique_together = [
            ['category', 'product']
        ]
