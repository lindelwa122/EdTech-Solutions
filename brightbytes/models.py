from django.db import models
from django.contrib.auth.models import AbstractUser

from json import loads, dumps

# Create your models here.
class User(AbstractUser):
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Course(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100000)
    course = models.ForeignKey(Course, models.CASCADE, related_name='course')

    def __str__(self):
        return self.title

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, models.CASCADE, related_name='lesson')
    question = models.CharField(max_length=100)
    options = models.CharField(max_length=1000, blank=True)
    answer = models.IntegerField()

    def set_options(self, options_list):
        self.options = dumps(options_list)

    def get_options(self):
        return loads(self.options)
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = 'Quizzes'

class Progress(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name='user')
    lessons = models.ManyToManyField(Lesson, related_name="lessons_progress")

    class Meta:
        verbose_name_plural = 'Progress'
    