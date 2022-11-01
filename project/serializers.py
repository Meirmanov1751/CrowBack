from rest_framework import serializers, generics
from .models import Project, Categorie,Relations
from django.utils import timezone




class CategoriesSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = ['id','name','descriptoin']

class CategoriesSerialiserForProject(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = ['id']

class ProjectSerializers(serializers.ModelSerializer):
    likes_count=serializers.SerializerMethodField()
    rate=serializers.DecimalField(max_digits=3,decimal_places=2,read_only=True)
    Sum=serializers.IntegerField()

    def get_likes_count(self, instance):
        return Relations.objects.filter(project=instance, like=True).count()

    class Meta:
     model = Project
     fields = ['id','owner','image', 'title', 'description', 'published_data', 'need_money', 'till_data', 'categories',
              'status','likes_count','rate','Sum']





class relationsSerializers(serializers.ModelSerializer):

    class Meta:
        model=Relations
        fields=[ 'id','user','project','like', 'in_Projectmarks','rate']