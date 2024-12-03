from django.urls import path, include

from theProject2.criminals.views import CriminalDashboardView, AddCriminalView, approve_criminal

urlpatterns = [
    path('dashboard/', CriminalDashboardView.as_view(), name='criminal_dashboard'),
    path('add-criminal/', AddCriminalView.as_view(), name='add_criminal'),
    path('<int:pk>/', include([
        path('approve/', approve_criminal, name='approve'),
    ]))
]
