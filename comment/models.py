

import timezones
from django.db import models
from django.contrib.auth.models import AbstractUser, User



class Comment(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    creted_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.comment


class CommentRelasions(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_answer=models.ForeignKey(Comment,on_delete=models.CASCADE)
    answer=models.TextField()


    def __str__(self):
        return f'{self.comment_answer}:{self.answer}'
