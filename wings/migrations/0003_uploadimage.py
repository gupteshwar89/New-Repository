# Generated by Django 4.0.5 on 2022-07-12 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wings', '0002_remove_patient_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wings.patient')),
            ],
        ),
    ]
