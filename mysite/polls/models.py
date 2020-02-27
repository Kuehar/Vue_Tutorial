import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

"""
「はじめてのDjangoアプリ作成、その2」にて投票システムに必要な、
・問題についてのmodel
・選択肢のmodel
をそれぞれ作成
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pubulished_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pubulished_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
