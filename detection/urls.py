from django.urls import path
from .views import detect_spam

urlpatterns = [
    path("", detect_spam, name="detect_spam"),
]
