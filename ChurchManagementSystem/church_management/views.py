from django.shortcuts import render, redirect
from .models import Financial_Transaction, ChurchMember, ChurchProject
from django.contrib import messages
from django.db import models
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    total_tithes = Financial_Transaction.objects.filter(category='tithe').aggregate(total=models.Sum('amount'))['total'] or 0
    total_offerings = Financial_Transaction.objects.filter(category='offering').aggregate(total=models.Sum('amount'))['total'] or 0
    total_seed = Financial_Transaction.objects.filter(category='seed').aggregate(total=models.Sum('amount'))['total'] or 0

    projects = ChurchProject.objects.all()

    total_members = ChurchMember.objects.count()

    recent_transactions = Financial_Transaction.objects.order_by('-date')[:10]

    return render(request, 'church_management/dashboard.html', {
        'total_tithes': total_tithes,
        'total_offerings': total_offerings,
        'total_seed': total_seed,
        'projects': projects,
        'total_members': total_members,
        'recent_transactions': recent_transactions
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')
    return render(request, 'church_management/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')

# def add_tithe(request):
#     if request.method == 'POST':
#         amount = request.POST.get('amount')
#         member_id = request.POST.get('member')
#         date = request.POST.get('date')
        
#         try:
#             member = ChurchMember.objects.get(id=member_id)
#             Financial_Transaction.objects.create(
#                 amount=amount,
#                 category='tithe',
#                 member=member,
#                 date=date
#             )
#             messages.success(request, 'Tithe added successfully!')
#         except ChurchMember.DoesNotExist:
#             messages.error(request, 'Member not found!')
#         return redirect('dashboard')
    
#     members = ChurchMember.objects.all()
#     return render(request, 'church_management/add_tithe.html', {'members': members})

def add_offering(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        
        Financial_Transaction.objects.create(
            amount=amount,
            category='offering',
            date=date
        )
        messages.success(request, 'Offering added successfully!')
        return redirect('dashboard')
    return render(request, 'church_management/add_offering.html')

def add_seed(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        
        try:
            Financial_Transaction.objects.create(
                amount=amount,
                category='seed'
            )
            messages.success(request, 'Seed offering added successfully!')
        except ChurchMember.DoesNotExist:
            messages.error(request, 'Member not found!')
        return redirect('dashboard')
    
    members = ChurchMember.objects.all()
    return render(request, 'church_management/add_seed.html', {'members': members})

def add_member(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        occupation = request.POST.get('occupation')
        fellowship = request.POST.get('fellowship')
        
        ChurchMember.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            address=address,
            date_of_birth=date_of_birth,
            gender=gender,
            marital_status=marital_status,
            occupation=occupation,
            fellowship=fellowship
        )
        messages.success(request, 'Member added successfully!')
        return redirect('dashboard')
    members = ChurchMember.objects.all()
    return render(request, 'church_management/add_member.html', {
        'members': members
    })

def add_project(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        target_amount = request.POST.get('target_amount')
        start_date = request.POST.get('start_date')
        
        ChurchProject.objects.create(
            name=name,
            description=description,
            target_amount=target_amount,
            start_date=start_date,
        )
        messages.success(request, 'Project added successfully!')
        return redirect('dashboard')
    return render(request, 'church_management/add_project.html')

# Create similar views for offerings, seed, members, and projects

