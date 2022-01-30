from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListPointAPIView.as_view(), name='list_points'),
]
