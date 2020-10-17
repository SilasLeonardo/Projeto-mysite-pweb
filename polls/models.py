from datetime import timedelta

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(verbose_name='Texto da Questão',max_length=200)
    pub_date = models.DateTimeField('Data da Publicação')

    def was_published_recently(self):
        ontem = timezone.now() - timedelta(days=1)
        return self.pub_date >= ontem

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Questão')
    choice_text = models.CharField(verbose_name='Texto da Escolha', max_length=200)
    votes = models.IntegerField('Numero de Votos',  default=0)

    def __str__(self):
        return self.choice_text