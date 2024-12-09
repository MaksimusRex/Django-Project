from django.urls import path, include

from theProject2.crimes.views import add_crime, EditCrimeView, DeleteCrimeView, DetailCrimeView

urlpatterns = [
    path('<int:pk>/', include([
        path('details/', DetailCrimeView.as_view(), name='detail_crime'),
        path('edit/', EditCrimeView.as_view(), name='edit_crime'),
        path('delete/', DeleteCrimeView.as_view(), name='delete_crime'),
    ])),
    # Other URLs for your app
    path('<int:criminal_id>/add-crime/', add_crime, name='add_crime'),
]
