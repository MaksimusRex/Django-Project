from django.urls import path

from theProject2.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]