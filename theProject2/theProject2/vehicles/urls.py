from django.urls import path, include

from theProject2.vehicles.views import AddVehicleView, EditVehicleView, DeleteVehicleView, DetailVehicleView

urlpatterns = [
    path('<int:pk>/', include([
        path('details/', DetailVehicleView.as_view(), name='detail_vehicle'),
        path('edit/', EditVehicleView.as_view(), name='edit_vehicle'),
        path('delete/', DeleteVehicleView.as_view(), name='delete_vehicle'),
    ])),
    path('<int:criminal_id>/add-vehicle/', AddVehicleView.as_view(), name='add_vehicle'),
]