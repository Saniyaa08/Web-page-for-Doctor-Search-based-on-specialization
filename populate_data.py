import warnings
warnings.filterwarnings("ignore", message="Data Validation extension is not supported")
import os
import django
import pandas as pd
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectname.settings')
django.setup()

from appname.models import Doctor

def populate_data(excel_file):
    df = pd.read_excel(excel_file)
    
    for _, row in df.iterrows():
        name = row['Name']
        specialization = row['Specialization']
        sub_specialization=row['SubSpecialization']
        affiliation = row['Affiliation']
        email = row['Email-id']
        phone_no = row['Phone no']
        type_of_phone_contact = row['Type of Phone contact']
        region = row['Region']
        cost_to_serve = row['Cost to Serve']
        status = row['Status']
        category = row['Category']
        lead_source = row['Lead Source']
        current_system = row['Current System']
        last_action = row['Last Action']
        lead_priority = row['Lead Priority']
        sales_rep = row['Sales Rep']
        reason_to_buy = row['Reason to buy']
        subcategory_reasons_to_buy = row['Subcatagory of Reasons to buy']
        date_of_connect_presentation = row['Date of Connect / Presentation']
        if pd.isnull(date_of_connect_presentation) or not isinstance(date_of_connect_presentation, datetime.datetime):
            date_of_connect_presentation = datetime.date.today()

        # Create a Doctor instance and save it
        doctor = Doctor(
            Name=name,
            Specialization=specialization,
            Sub_Specialization= sub_specialization,
            Affiliation=affiliation,
            Emailid =email,
            Phoneno=phone_no,
            type_of_phone_contact=type_of_phone_contact,
            region=region,
            cost_to_serve=cost_to_serve,
            status=status,
            category=category,
            lead_source=lead_source,
            current_system=current_system,
            last_action=last_action,
            lead_priority=lead_priority,
            date_of_connect_presentation=date_of_connect_presentation,
            sales_rep=sales_rep,
            reason_to_buy=reason_to_buy,
            subcategory_reasons_to_buy=subcategory_reasons_to_buy
        )
        doctor.save()


if __name__ == '__main__':
    excel_file = "C:/Users/DELL/Downloads/Dataset_CRM_0206_Rev00 (1).xlsx"
    populate_data(excel_file)
