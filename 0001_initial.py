# Generated by Django 4.2 on 2023-06-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=100)),
                ('SPECIALIZATION', models.CharField(max_length=100)),
                ('AFFILIATION', models.CharField(max_length=100)),
                ('EMAILID', models.CharField(max_length=100)),
                ('Phoneno', models.CharField(max_length=20)),
                ('type_of_phone_contact', models.CharField(max_length=100, verbose_name='Type of Phone Contact')),
                ('region', models.CharField(max_length=100)),
                ('cost_to_serve', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('category', models.CharField(default='Default Category', max_length=100)),
                ('lead_source', models.CharField(max_length=100)),
                ('current_system', models.CharField(max_length=100)),
                ('last_action', models.CharField(max_length=100)),
                ('lead_priority', models.CharField(max_length=100)),
                ('date_of_connect_presentation', models.DateField(blank=True, null=True, verbose_name='Date of Connect / Presentation')),
                ('sales_rep', models.CharField(max_length=100, verbose_name='Sales Rep')),
                ('reason_to_buy', models.TextField(verbose_name='Reason to Buy')),
                ('subcategory_reasons_to_buy', models.CharField(max_length=100, verbose_name='Subcategory of Reasons to Buy')),
            ],
        ),
    ]
