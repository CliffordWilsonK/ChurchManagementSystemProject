from django.contrib import admin
from church_management.models import Financial_Transaction, ChurchProject, ChurchMember

# Register your models here.
admin.site.register(Financial_Transaction)
admin.site.register(ChurchProject)
admin.site.register(ChurchMember)
