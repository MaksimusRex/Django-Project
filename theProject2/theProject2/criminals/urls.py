from django.urls import path

from theProject2.criminals.views import CriminalDashboardView, AddCriminalView

urlpatterns = [
    path('dashboard/', CriminalDashboardView.as_view(), name='criminal_dashboard'),
    path('add-criminal/', AddCriminalView.as_view(), name='add_criminal'),
]