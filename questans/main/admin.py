from django.contrib import admin
from .models import FAQ  # Import the FAQ model
from django.utils.html import format_html  # To display formatted text in admin

@admin.register(FAQ)  # Register the FAQ model
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'translated_question_hi', 'translated_question_bn', 'formatted_answer')  # Fields displayed in list
    search_fields = ('question',)  # Search based on English question
    list_filter = ('question',)  # Filter FAQs

    def translated_question_hi(self, obj):
        return obj.get_translated_text("hi")["question"]
    translated_question_hi.short_description = "Question (Hindi)"

    def translated_question_bn(self, obj):
        return obj.get_translated_text("bn")["question"]
    translated_question_bn.short_description = "Question (Bengali)"

    def formatted_answer(self, obj):
        return format_html(obj.answer)  # Display formatted answer
    formatted_answer.short_description = "Formatted Answer"
