# Generated by Django 3.0.5 on 2020-04-05 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipmodel',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
