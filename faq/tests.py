from django.test import TestCase # type: ignore
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a Python framework.")

    def test_translation(self):
        self.assertEqual(self.faq.get_translated_question('en'), "What is Django?")
