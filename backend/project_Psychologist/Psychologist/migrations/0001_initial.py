# Generated by Django 5.0.2 on 2024-03-10 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Psychologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.PositiveIntegerField(unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=15)),
                ('document', models.CharField(max_length=15, null=True, unique=True)),
                ('start_time_morning', models.TimeField()),
                ('end_time_morning', models.TimeField()),
                ('start_time_afternoon', models.TimeField()),
                ('end_time_afternoon', models.TimeField()),
            ],
            options={
                'db_table': 'psychologist',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_patient', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Requested', 'Requested'), ('Awaiting Payment', 'Awaiting Payment'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Requested', max_length=20)),
                ('scheduled_time', models.DateTimeField()),
                ('payment_proof', models.FileField(blank=True, null=True, upload_to='payment_proofs/')),
                ('psychologist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='Psychologist.psychologist')),
            ],
        ),
        migrations.AddConstraint(
            model_name='consultation',
            constraint=models.UniqueConstraint(fields=('psychologist', 'scheduled_time'), name='unique_scheduled_time_for_psychologist'),
        ),
        migrations.AddConstraint(
            model_name='consultation',
            constraint=models.UniqueConstraint(fields=('id_patient', 'scheduled_time'), name='unique_scheduled_time_for_patient'),
        ),
    ]