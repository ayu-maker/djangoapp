from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ

class FAQListAPIView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")  # Default to English
        cached_data = cache.get(f"faqs_{lang}")  # Check cache

        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        translated_faqs = [faq.get_translated_text(lang) for faq in faqs]

        cache.set(f"faqs_{lang}", translated_faqs, timeout=3600)  # Cache for 1 hour

        return Response(translated_faqs)
