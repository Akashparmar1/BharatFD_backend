from rest_framework import viewsets# type: ignore
from rest_framework.response import Response# type: ignore
from django.core.cache import cache# type: ignore
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        cache.set(cache_key, serializer.data, timeout=3600)
        return Response(serializer.data)
