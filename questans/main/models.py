from django.db import models
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def get_translated_text(self, lang):
        """Translate question and answer dynamically based on language selection."""
        if lang == "en":
            return {"question": self.question, "answer": self.answer}
        
        translator = Translator()
        translated_question = translator.translate(self.question, dest=lang).text
        translated_answer = translator.translate(self.answer, dest=lang).text

        return {"question": translated_question, "answer": translated_answer}

    def __str__(self):
        return self.question
