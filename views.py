from django.shortcuts import render, redirect , HttpResponse
from .models import Doctor , SubSpecialization 
from .forms import DoctorForm
from django.db.models import Q
from django.db.models import Count

def search(request):
    form = DoctorForm(request.GET)
    doctors = Doctor.objects.all()
    

    if form.is_valid():
        name = form.cleaned_data.get('name')
        affiliation = form.cleaned_data.get('affiliation')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        sub_specialization=form.cleaned_data.get('sub_specialization')
        specialization = form.cleaned_data.get('specialization')
        type_of_phone_contact = form.cleaned_data.get('type_of_phone_contact')
        region = form.cleaned_data.get('region')
        cost_to_serve = form.cleaned_data.get('cost_to_serve')
        status = form.cleaned_data.get('status')
        category = form.cleaned_data.get('category')
        lead_source = form.cleaned_data.get('lead_source')
        current_system = form.cleaned_data.get('current_system')
        last_action = form.cleaned_data.get('last_action')
        lead_priority = form.cleaned_data.get('lead_priority')
        date_of_connect_presentation = form.cleaned_data.get('date_of_connect_presentation')
        sales_rep = form.cleaned_data.get('sales_rep')
        reason_to_buy = form.cleaned_data.get('reason_to_buy')
        subcategory_reasons_to_buy = form.cleaned_data.get('subcategory_reasons_to_buy')

        if name:
            doctors = doctors.filter(Q(Name__icontains=name))
        if affiliation:
            doctors = doctors.filter(Q(Affiliation__icontains=affiliation))
        if email:
            doctors = doctors.filter(Q(Emailid__icontains=email))
        if phone:
            doctors = doctors.filter(Q(Phoneno__icontains=phone))
        if specialization:
            doctors = doctors.filter(Q(Specialization__icontains=specialization))
        if type_of_phone_contact:
            doctors = doctors.filter(Q(type_of_phone_contact__icontains=type_of_phone_contact))
        if region:
            doctors = doctors.filter(Q(region__icontains=region))
        if cost_to_serve:
            doctors = doctors.filter(Q(cost_to_serve=cost_to_serve))
        if status:
            doctors = doctors.filter(Q(status__icontains=status))
        if category:
            doctors = doctors.filter(Q(category__icontains=category))
        if lead_source:
            doctors = doctors.filter(Q(lead_source__icontains=lead_source))
        if current_system:
            doctors = doctors.filter(Q(current_system__icontains=current_system))
        if last_action:
            doctors = doctors.filter(Q(last_action__icontains=last_action))
        if lead_priority:
            doctors = doctors.filter(Q(lead_priority__icontains=lead_priority))
        if date_of_connect_presentation:
            doctors = doctors.filter(Q(date_of_connect_presentation=date_of_connect_presentation))
        if sales_rep:
            doctors = doctors.filter(Q(sales_rep__icontains=sales_rep))
        if reason_to_buy:
            doctors = doctors.filter(Q(reason_to_buy__icontains=reason_to_buy))
        if subcategory_reasons_to_buy:
            doctors = doctors.filter(Q(subcategory_reasons_to_buy__icontains=subcategory_reasons_to_buy))
            request.session['search_form_data'] = request.GET

        else:
             form_data = request.session.get('search_form_data', {})
             form = DoctorForm(form_data)

    doctors = Doctor.objects.all()

            # Count the number of doctors for each specialization
    specialization_count = doctors.values('Specialization').annotate(total=Count('id'))



    context = {'form': form, 'doctors': doctors}
    return render(request, 'search.html', context)



def graph(request):
    specialization_count = Doctor.objects.values('Specialization').annotate(total=Count('id'))

    context = {'specialization_count': specialization_count}
    return render(request, 'graph.html', context)


def sub_specialization_graph(request):
    specialization = request.GET.get('specialization', 'all')

    if specialization == 'all':
        sub_specialization_count = SubSpecialization.objects.values('Sub_Specialization').annotate(total=Count('Sub_Specialization'))
    else:
        sub_specialization_count = SubSpecialization.objects.filter(Specialization=specialization).values('Sub_Specialization').annotate(total=Count('Sub_Specialization'))

    return render(request, 'sub_specialization_graph.html', {'sub_specialization_count': sub_specialization_count, 'selected_specialization': specialization})




def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = Doctor(
                Name=form.cleaned_data['name'],
                Specialization=form.cleaned_data['specialization'],

                Affiliation=form.cleaned_data['affiliation'],
                Emailid=form.cleaned_data['email_id'],
                Phoneno=form.cleaned_data['phone_no'],
                region=form.cleaned_data['region'],
                cost_to_serve=form.cleaned_data['cost_to_serve'],
                status=form.cleaned_data['status'],
                category=form.cleaned_data['category']
            )
            doctor.save()
            return redirect('success')
    else:
        form = DoctorForm()

    return render(request, 'add_doctor.html', {'form': form})

def success(request):
    return render(request, 'success.html')

from .models import AdminData

def admin_dashboard(request):
    admin_data = AdminData.objects.all()
    context = {'admin_data': admin_data}
    return render(request, 'admin_dashboard.html', context)

from .models import User1Data

def user1_dashboard(request):
    user1_data = User1Data.objects.all()
    context = {'user1_data': user1_data}
    return render(request, 'user1_dashboard.html', context)


from .models import User2Data

def user2_dashboard(request):
    user2_data = User2Data.objects.all()
    context = {'user2_data': user2_data}
    return render(request, 'user2_dashboard.html', context)


from django.contrib.auth import authenticate, login

def admin_login(request):
    if request.method == 'POST':
        admin_username = request.POST.get('admin_username')
        admin_password = request.POST.get('admin_password')
        user = authenticate(request, username=admin_username, password=admin_password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            # Handle invalid credentials
            return HttpResponse('Invalid username or password')
    return render(request, 'admin_login.html')
from django.contrib.auth import authenticate, login

def user1_login(request):
    if request.method == 'POST':
        user1_username = request.POST.get('user1_username')
        user1_password = request.POST.get('user1_password')
        user = authenticate(request, username=user1_username, password=user1_password)
        if user is not None:
            login(request, user)
            return redirect('user1_dashboard')
        else:
            # Handle invalid credentials
            return HttpResponse('Invalid username or password')
    return render(request, 'user1_login.html')
from django.contrib.auth import authenticate, login

def user2_login(request):
    if request.method == 'POST':
        user2_username = request.POST.get('user2_username')
        user2_password = request.POST.get('user2_password')
        user = authenticate(request, username=user2_username, password=user2_password)
        if user is not None:
            login(request, user)
            return redirect('user2_dashboard')
        else:
            # Handle invalid credentials
            return HttpResponse('Invalid username or password')
    return render(request, 'user2_login.html')

