from rest_framework import serializers, generics
from .models import Comment,CommentRelasions
from django.utils import timezone




class CommentSerialiser(serializers.ModelSerializer):
    answer=serializers.SerializerMethodField()

    def get_answer(self,instance):
        return CommentRelasions.objects.filter(comment_answer=instance).get()

    class Meta:
        model = Comment
        fields = ['id','comment','creted_date','update_date','answer']

class CommentRelSerialiser(serializers.ModelSerializer):


    class Meta:
        model = CommentRelasions
        fields = ['id','user_id','comment_answer','answer']


