# Generated by Django 3.1.2 on 2020-10-07 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_category_comission_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('category', models.ForeignKey(db_column='id_category', on_delete=django.db.models.deletion.DO_NOTHING, to='core.category')),
                ('product', models.ForeignKey(db_column='id_product', on_delete=django.db.models.deletion.DO_NOTHING, to='core.product')),
            ],
            options={
                'db_table': 'product_category',
                'managed': True,
            },
        ),
    ]