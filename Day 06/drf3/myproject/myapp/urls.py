from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdatesDestroyView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdatesDestroyView.as_view(), name='student-retrieve-update-destroy'),
]
