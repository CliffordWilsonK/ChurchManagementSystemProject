from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('add-tithe/', views.add_tithe, name='add_tithe'),
    path('add-offering/', views.add_offering, name='add_offering'),
    path('add-seed/', views.add_seed, name='add_seed'),
    path('add-member/', views.add_member, name='add_member'),
    path('add-project/', views.add_project, name='add_project'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]