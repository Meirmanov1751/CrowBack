
from rest_framework import serializers
from rest_framework.utils import json

from project.models import Project
from .models import ProjectPlan,ProjectBacked


class ProjectPlanSerialaizers(serializers.ModelSerializer):


    class Meta:
        model=ProjectPlan
        fields=['id','amount','rewards','description','project']



class ProjectBackedSerialaizers(serializers.ModelSerializer):


    class Meta:
        model=ProjectBacked
        fields=['id','status','project_plan','user_id','created_date']

