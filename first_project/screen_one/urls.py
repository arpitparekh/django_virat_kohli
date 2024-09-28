from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.show_dashboard, name='dashboard'),
    path('pass_data/', views.show_pass_data, name='pass_data'),
]
