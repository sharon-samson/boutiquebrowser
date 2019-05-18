# Generated by Django 2.1.3 on 2018-11-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Saree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500)),
                ('product_id', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('product_detail', models.CharField(max_length=5000)),
                ('length', models.DecimalField(decimal_places=4, max_digits=5)),
                ('category', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount_rate', models.IntegerField()),
                ('discount_percent', models.DecimalField(decimal_places=4, max_digits=5)),
                ('stock_balance', models.PositiveIntegerField()),
                ('dispatch_in', models.PositiveIntegerField(blank=True, choices=[(0, 'Instant'), (1, 'In 1-2 Days'), (2, 'In 7-8 Days'), (3, 'In 30 days')], null=True)),
                ('free_shipping', models.BooleanField(default=False)),
                ('care', models.CharField(max_length=100)),
            ],
        ),
    ]