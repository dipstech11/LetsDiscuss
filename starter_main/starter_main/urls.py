from django.contrib import admin
from django.urls import path
from boards import views

urlpatterns = [
    path(r'', views.home, name="home"),
    path(r'boards/<int:pk>', views.board_topics, name='board_topic'),
    path(r'boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('admin/', admin.site.urls),
]
