from django.urls import path
from .views import SetupDatasetView

urlpatterns = [
    path('dataset', SetupDatasetView.as_view(), name='setup-dataset-no-slash'),
    path('dataset/', SetupDatasetView.as_view(), name='setup-dataset'),
]
