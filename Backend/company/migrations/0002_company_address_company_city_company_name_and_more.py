# Generated by Django 5.0.1 on 2024-02-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='zipcode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
