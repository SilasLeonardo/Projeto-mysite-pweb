from datetime import timedelta
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(verbose_name='Texto da Questão',max_length=200,
                                     help_text="Informe o texto da Questão")
    pub_date = models.DateTimeField('Data da Publicação', default=timezone.now)

    def was_published_recently(self):
        ontem = timezone.now() - timedelta(days=1)
        return self.pub_date >= ontem

    def __str__(self):
        return self.question_text

    @property
    def maior_choice(self):
        maior = self.choice_set.aggregate(models.Max('votes'))['votes__max']
        return self.choice_set.get(votes__exact=maior)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Questão')
    choice_text = models.CharField('Texto da Escolha', max_length=200)
    votes = models.IntegerField('Numero de Votos',  default=0)
    pub_date = models.DateTimeField('Data de publicacao', default=timezone.now)

    def was_published_recently_Choice(self):
        ontem = timezone.now() - timedelta(days=1)
        return self.pub_date >= ontem

    def __str__(self):
        return self.choice_text