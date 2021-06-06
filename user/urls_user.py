from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('register', RegisterModelView)
urlpatterns = [
    path('', include(router.urls), name='register'),
    path('login/', AuthView.as_view(), name='login'),
    path('user/', ClientView.as_view()),
    path('worker/', WorkerView.as_view())
]
