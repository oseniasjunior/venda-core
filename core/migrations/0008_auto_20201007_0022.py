# Generated by Django 3.1.2 on 2020-10-07 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_category_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(through='core.ProductCategory', to='core.Category'),
        ),
    ]
