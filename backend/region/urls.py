from django.urls import path

from .views import SeoulGuListView

urlpatterns = [
    path('', SeoulGuListView.as_view()),
]
