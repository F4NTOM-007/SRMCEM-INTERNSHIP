from django.urls import path,include
from rest_framework import routers
from .views import BlogViewSet, blog_ui

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('user/', include(router.urls)), #Full CRUD at /user/blogs/
    path('blog_ui/', blog_ui, name='blog-ui'), #only for UI rendering
]
