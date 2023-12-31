from django import forms

class DoctorForm(forms.Form):
    name = forms.CharField(label='Name', required=False)
    affiliation = forms.CharField(label='Affiliation', required=False)
    email = forms.EmailField(label='Emailid', required=False)
    phone = forms.CharField(label='Phoneno', required=False)
    specialization = forms.CharField(label='Specialization', required=False)
    Sub_Specialization = forms.CharField(label='SubSpecialization', required=False)
    type_of_phone_contact = forms.CharField(label='Type of Phone Contact', required=False)
    region = forms.CharField(label='Region', required=False)
    cost_to_serve = forms.DecimalField(label='Cost to Serve', required=False)
    status = forms.CharField(label='Status', required=False)
    category = forms.CharField(label='Category', required=False)
    lead_source = forms.CharField(label='Lead Source', required=False)
    current_system = forms.CharField(label='Current System', required=False)
    last_action = forms.CharField(label='Last Action', required=False)
    lead_priority = forms.CharField(label='Lead Priority', required=False)
    date_of_connect_presentation = forms.DateField(label='Date of Connect / Presentation', required=False)
    sales_rep = forms.CharField(label='Sales Rep', required=False)
    reason_to_buy = forms.CharField(label='Reason to Buy', required=False)
    subcategory_reasons_to_buy = forms.CharField(label='Subcategory of Reasons to Buy', required=False)
