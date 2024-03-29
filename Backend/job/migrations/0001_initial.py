# Generated by Django 5.0.1 on 2024-02-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0002_company_address_company_city_company_name_and_more'),
        ('employee', '0003_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('company', models.ManyToManyField(to='company.company')),
                ('employee', models.ManyToManyField(to='employee.employee')),
            ],
        ),
    ]
