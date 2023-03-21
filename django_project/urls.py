from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from sig.views import base_views

urlpatterns = [
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('admin/', admin.site.urls),
    path('sig/', include('sig.urls')),
    path('common/', include('common.urls')),
]
