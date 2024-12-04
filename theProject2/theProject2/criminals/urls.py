from django.urls import path, include

from theProject2.criminals.views import CriminalDashboardView, AddCriminalView, approve_criminal, \
    EditCriminalDetailInfoView, CriminalDetailView

urlpatterns = [
    path('dashboard/', CriminalDashboardView.as_view(), name='criminal_dashboard'),
    path('add-criminal/', AddCriminalView.as_view(), name='add_criminal'),
    path('<int:pk>/', include([
        path('approve/', approve_criminal, name='approve'),
        path('criminal-details/', CriminalDetailView.as_view(), name='criminal_details'),
        path('edit-criminal-details/', EditCriminalDetailInfoView.as_view(), name='edit_details'),
    ]))
]
