# Generated by Django 3.0.5 on 2020-04-07 15:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InternshipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('days_ago_posted', models.CharField(max_length=100)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.CompanyModel')),
            ],
        ),
    ]
