from django.db import models

class Doctor(models.Model):
    Name= models.CharField(max_length=100)
    Specialization = models.CharField(max_length=100)
    Sub_Specialization = models.CharField(max_length=100)
    Affiliation= models.CharField(max_length=100)
    Emailid= models.CharField(max_length=100)
    Phoneno= models.CharField(max_length=20)

    type_of_phone_contact = models.CharField(max_length=100, verbose_name="Type of Phone Contact")
    region = models.CharField(max_length=100)
    cost_to_serve = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='Default Category')
    lead_source = models.CharField(max_length=100)
    current_system = models.CharField(max_length=100)
    last_action = models.CharField(max_length=100)
    lead_priority = models.CharField(max_length=100)
    date_of_connect_presentation = models.DateField(verbose_name="Date of Connect / Presentation", null=True, blank=True)
    sales_rep = models.CharField(max_length=100, verbose_name="Sales Rep")
    reason_to_buy = models.TextField(verbose_name="Reason to Buy")
    subcategory_reasons_to_buy = models.CharField(max_length=100, verbose_name="Subcategory of Reasons to Buy")

    def __str__(self):
        return self.name

class AdminData(models.Model):
    username = models.CharField(max_length=100,default='your_default_value')
    password = models.CharField(max_length=100)
class User1Data(models.Model):
    username = models.CharField(max_length=100,default='your_default_value')
    password = models.CharField(max_length=100)
class User2Data(models.Model):
    username = models.CharField(max_length=100,default='your_default_value')
    password = models.CharField(max_length=100)


from django.db import models

class SubSpecialization(models.Model):
    Specialization = models.CharField(max_length=255)
    Sub_Specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.Sub_Specialization
