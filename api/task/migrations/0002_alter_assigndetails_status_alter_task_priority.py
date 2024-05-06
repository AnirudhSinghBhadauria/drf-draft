# Generated by Django 5.0.4 on 2024-05-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigndetails',
            name='status',
            field=models.CharField(choices=[('APPROVED', 'Approved'), ('PENDING', 'Pending'), ('REJECTED', 'Rejected')], default='PENDING', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low')], default='MEDIUM', max_length=50),
        ),
    ]
