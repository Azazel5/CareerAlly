# Generated by Django 3.0.5 on 2020-04-10 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinternshipprofile',
            name='application_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinternshipprofile',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
