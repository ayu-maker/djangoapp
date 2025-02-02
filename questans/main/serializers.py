from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']  # Only include translated data

    def get_question(self, obj):
        lang = self.context.get('lang', 'en')  # Get language from context
        return obj.get_translated_data(lang)['question']

    def get_answer(self, obj):
        lang = self.context.get('lang', 'en')  # Get language from context
        return obj.get_translated_data(lang)['answer']
