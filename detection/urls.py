from django.urls import path
from .views import detect_spam
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path("", detect_spam, name="detect_spam"),
]
#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

