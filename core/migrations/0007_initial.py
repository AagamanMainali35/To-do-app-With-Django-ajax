# Generated by Django 5.0.7 on 2024-08-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0006_remove_patient_p_d_details_delete_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(blank=True, max_length=400, null=True, verbose_name='Taskname')),
            ],
        ),
    ]