# Generated by Django 3.1.2 on 2020-10-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_employee_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(db_column='salary', decimal_places=2, default=0, max_digits=10),
        ),
    ]
