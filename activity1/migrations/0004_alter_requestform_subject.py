# Generated by Django 4.2 on 2023-06-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity1', '0003_alter_requestform_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestform',
            name='subject',
            field=models.CharField(choices=[('', 'Select a subject'), ('option1', 'Driver for Long Rides'), ('option2', 'Third wheel for Dates'), ('option3', 'Gym Buddy / Coach')], max_length=20),
        ),
    ]
