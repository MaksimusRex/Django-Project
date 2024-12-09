from django.urls import path
from .views import PrisonCreateView

urlpatterns = [
    path('create/', PrisonCreateView.as_view(), name='create_prison'),

]