from django.urls import path
from .views import UserSignupView, UserSignupDetailView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user_signup'),
    path('signup/<int:pk>/', UserSignupDetailView.as_view(), name='user_signup_detail'),
]
