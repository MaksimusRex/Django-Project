from django.urls import path

from theProject2.crimes.views import add_crime

urlpatterns = [
    # Other URLs for your app
    path('<int:criminal_id>/add-crime/', add_crime, name='add_crime'),
]
