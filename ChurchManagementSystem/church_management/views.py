from django.shortcuts import render
from .models import Financial_Transaction, ChurchMember, ChurchProject
from django.db import models

# Create your views here.
def dashboard(request):
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

