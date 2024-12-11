from django.urls import path, include
from .views import PrisonCreateView, PrisonListView, EditPrisonView, DetailPrisonView, DeletePrisonView

urlpatterns = [
    path('create/', PrisonCreateView.as_view(), name='create_prison'),
    path('dashboard/', PrisonListView.as_view(), name='prisons_dashboard'),
    path('<int:pk>/', include([
        path('edit', EditPrisonView.as_view(), name='edit_prison'),
        path('details/', DetailPrisonView.as_view(), name='detail_prison'),
        path('delete/', DeletePrisonView.as_view(), name='delete_prison'),
    ])),
]