"""from django.urls import path
from .views import UserSignupView, UserSignupDetailView, UserLoginView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user_signup'),
    path('signup/<int:pk>/', UserSignupDetailView.as_view(), name='user_signup_detail'),
    path('login/', UserLoginView.as_view(), name='user_login'),
]

"""

from django.urls import path
from .views import signup, login_view, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
