from django.db import models
from django.contrib.auth import get_user_model
import random


class CategotyQuiz(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/',)
    body = models.TextField()
    def __str__(self):
        return self.name
DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    cat = models.ForeignKey(CategotyQuiz, on_delete=models.CASCADE)
    topic = models.CharField(max_length=150)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Testke qansha waqit kerek")
    required_score_to_pass = models.IntegerField(help_text="otiw procenti %")
    difficluty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Testler'
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()
    class Meta:
        verbose_name_plural = 'Sorawlar'
class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"
    class Meta:
        verbose_name_plural = 'juwaplar'
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    user = models.ForeignKey(get_user_model() , on_delete = models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f'{self.pk} {self.quiz} {self.score}'
    class Meta:
        verbose_name_plural = 'Natiyjeler'