from django.contrib.auth.models import AbstractUser
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    quizzesCreated = models.IntegerField(default=0)
    quizzesCompleted = models.IntegerField(default=0)
    correctAnswers = models.IntegerField(default=0)
    incorrectAnswers = models.IntegerField(default=0)
    averageScore = models.FloatField(null=True, blank=True)
    bestCategory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="best")
    worstCategory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="worst")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.username,
            "quizzesCreated": self.quizzesCreated,
            "quizzesCompleted": self.quizzesCompleted,
            "correctAnswers": self.correctAnswers,
            "averageScore": self.averageScore,
        }

    def __str__(self):
        return self.username

class Quiz(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="quizzes")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    questionNumber = models.IntegerField()
    timestamp = models.DateTimeField()

    def serialize(self):
        return {
            "id": self.id,
            "creator_id": self.creator.id,
            "creator": self.creator.username,
            "category_id": self.category.id,
            "category": self.category.name,
            "name": self.name,
            "description": self.description,
            "questionNumber": self.questionNumber,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="results")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="results")
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.quiz.name} ({self.percentage}%)"

class Answer(models.Model):
    number = models.IntegerField()
    answer = models.CharField(max_length=1000)
    correct = models.BooleanField()

    def __str__(self):
        return f"{self.answer} ({self.number})"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    number = models.IntegerField()
    question = models.CharField(max_length=1000)
    answers = models.ManyToManyField(Answer, blank=True)

    def __str__(self):
        return f"{self.question} ({self.number})"
