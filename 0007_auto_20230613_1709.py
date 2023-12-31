# Generated by Django 4.2 on 2023-06-13 11:39

from django.db import migrations , models

def set_default_sub_specialization(apps, schema_editor):
    Doctor = apps.get_model('appname', 'Doctor')
    Doctor.objects.update(Sub_Specialization='default_value')


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0006_rename_data_admindata_password_and_more'),
    ]

    operations = [
         migrations.AddField(
            model_name='doctor',
            name='Sub_Specialization',
            field=models.CharField(default='default_value', max_length=255),
            preserve_default=False,
        ),
        migrations.RunPython(set_default_sub_specialization),
    ]
    
