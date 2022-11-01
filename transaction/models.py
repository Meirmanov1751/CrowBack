from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

from project.models import Project

class ProjectPlan(models.Model):
    amount=models.IntegerField()
    rewards=models.IntegerField()
    description=models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.project}'


class ProjectBacked(models.Model):
    class STATUSES:
        PROCEEDING = 'proceeding'
        SUCCESS = 'success'
        FAIL = 'fail'
        STATUS_CHOICES = [(PROCEEDING, 'В обработке'), (SUCCESS, 'Успешная Оплата'), (FAIL, 'Не успешная оплата')]
    status = models.CharField(choices=STATUSES.STATUS_CHOICES, default=STATUSES.PROCEEDING, max_length=300)
    project_plan=models.ForeignKey(ProjectPlan,on_delete=models.CASCADE,blank=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    created_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.status}:{self.created_date}'

