from django.test import TestCase
from django.utils import timezone

from .models import Question


# Create your tests here.


class QuestionModelTestCase(TestCase):

    def test_string_representation(self):
        question = Question.objects.create(
            question_text="did this test work?", pub_date=timezone.now())
        self.assertEqual(question.question_text, "did this test work?")
