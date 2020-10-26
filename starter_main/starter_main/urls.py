from django.contrib import admin
from django.urls import path
from boards import views

urlpatterns = [
    path(r'', views.home, name="home"),
    path('admin/', admin.site.urls),
]
