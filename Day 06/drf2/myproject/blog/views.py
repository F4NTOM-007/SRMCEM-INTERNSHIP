from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Blog
from .serializers import BlogSerializer
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.
class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# Add missing blog_ui view
from django.http import HttpResponse
def blog_ui(request):
    return HttpResponse("Blog UI placeholder")
    