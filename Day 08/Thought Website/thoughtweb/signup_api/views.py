from django.shortcuts import render

from rest_framework import generics
from .models import UserSignup
from .serializers import UserSignupSerializer
from .serializers import UserLoginSerializer
from .models import UserLogin

class UserSignupView(generics.ListCreateAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignupSerializer

class UserSignupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignupSerializer


# Login view
class UserLoginView(generics.CreateAPIView):
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer