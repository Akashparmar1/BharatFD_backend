from django.db import models # type: ignore
from ckeditor.fields import RichTextField # type: ignore
from googletrans import Translator # type: ignore

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    language = models.CharField(max_length=10, default='en')

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)

    def __str__(self):
        return self.question
