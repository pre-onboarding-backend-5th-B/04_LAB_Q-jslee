from django.urls import path

from .views import get_flooding

urlpatterns = [
    path('<str:gu_name>/', get_flooding),
]
