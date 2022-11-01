from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User
from future.backports.datetime import timedelta


class Categorie(models.Model):
    name = models.CharField(max_length=200)
    descriptoin = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.name}:{self.descriptoin}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Project(models.Model):
        owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='user'
                                )
        image = models.ImageField(blank=True)
        title = models.CharField(max_length=200)
        description = models.CharField(max_length=200)
        published_data = models.DateTimeField(auto_now_add=True)
        update_date = models.DateTimeField(auto_now=True)
        need_money = models.IntegerField(default=1000)

        till_date_duration=((timedelta(days=10),'малый срок'),(timedelta(days=21),'среднии срок'),(timedelta(days=31),'большой срок'))


        till_data = models.DurationField(choices=till_date_duration)
        categories = models.ForeignKey(Categorie,on_delete=models.CASCADE,blank=True)

        class STATUS:
            ACTIVE = 'active'
            FINISHED = 'finished'
            CANCELED = 'canceled'
            CHOICES = [(ACTIVE, 'active'), (FINISHED, 'finished'), (CANCELED, 'canceled')]

        status = models.TextField(choices=STATUS.CHOICES, default=STATUS.ACTIVE)
        project_invest = models.ManyToManyField(User, through='Relations',related_name='project')


        def __str__(self):
            return f'{self.title}:{self.status}'

        class Meta:
            verbose_name = 'Проект'
            verbose_name_plural = 'Проеты'

class Relations(models.Model):


    rate_project=((1,'shit'),
                  (2,'some shit'),
                  (3,'norm'),
                  (4,'good'),
                  (5,'cool')
                  )

    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    project= models.ForeignKey(Project, on_delete=models.CASCADE, blank=True)
    like=models.BooleanField(default=False)
    in_projectmarks=models.BooleanField(default=False)
    rate=models.PositiveSmallIntegerField(choices=rate_project)
    money=models.IntegerField(default=100)

    def __str__(self):
        return f'{self.user.username}:{self.project}'