# Generated by Django 3.1 on 2020-10-22 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientPrec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prec', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loginweb.patientregister')),
            ],
        ),
    ]
