from django.urls import path, include
from .views import ToBookClientView

urlpatterns = [
    path('', ToBookClientView.as_view())
]
