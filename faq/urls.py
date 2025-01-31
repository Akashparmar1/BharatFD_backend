from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter# type: ignore
from .views import FAQViewSet

router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

