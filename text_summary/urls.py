from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),  # 'upload' ビューが存在する場合
]
