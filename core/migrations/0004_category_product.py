# Generated by Django 3.1.2 on 2020-10-06 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=104)),
            ],
            options={
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=104)),
                ('price', models.DecimalField(db_column='price', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
    ]
