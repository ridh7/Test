from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):
    question = models.TextField()
    question_title = models.TextField()

    def __str__(self):
        return self.question_title + '-' + self.question


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    question = models.ManyToManyField(Questions)


class Submissions(models.Model):
    code = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
