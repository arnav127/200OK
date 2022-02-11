# Generated by Django 3.2.12 on 2022-02-11 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicinePrescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=255, verbose_name='Medicine Name')),
                ('doses', models.CharField(blank=True, max_length=255, verbose_name='Doses')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.patient')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientrecord.medicineprescription')),
            ],
        ),
    ]
