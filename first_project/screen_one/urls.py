from django.urls import path
from . import views

urlpatterns = [
    path('show_text/',views.show_text,name='show_text')
]
