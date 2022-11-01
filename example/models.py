from django.db import models


# Create your models here.

# Все классы начинаются с больщой буквы, все функции (def) начинаются с маленькой
# Константы должны быть с большой буквы
class ExampleRelatedModel(models.Model):
    name = models.CharField(max_length=300)


class Example(models.Model):
    class STATUS:
        OPEN = 'open'
        CLOSED = 'closed'
        CHOICES = [(OPEN, 'открыто'), (CLOSED, 'закрыто')]

    status = models.TextField(choices=STATUS.CHOICES, default=STATUS.OPEN)
    name = models.CharField(max_length=300)
    related_model = models.ForeignKey(ExampleRelatedModel,on_delete=models.CASCADE)