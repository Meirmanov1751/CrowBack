from django.db.models import Count,Sum
from django.shortcuts import render


import django_filters
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from djangochannelsrestframework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import GenericViewSet
#from .filters import CategoriesFilter #BookmarkFilter,CategoriesFilter
from project.models import Project, Relations
from .serializers import ProjectPlanSerialaizers,ProjectBackedSerialaizers
from .models import ProjectPlan,ProjectBacked
from rest_framework import mixins, viewsets,permissions

#ProjectBackedSerialaizers

class ProjectBackedViewSet(mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                           mixins.CreateModelMixin, GenericViewSet):
        serializer_class =ProjectBackedSerialaizers
        queryset = ProjectBacked.objects.all()



class ProjectPlanViewSet(mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                             mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ProjectPlanSerialaizers
    queryset = ProjectPlan.objects.all().annotate(
        project1=Count('project__title')
    )
    #filter_class =
    permission_classes = [permissions.IsAuthenticated]

#@action(methods=['post'], detail=True)
    #def buy(self, request, *args, **kwargs):
   #    request_serializers=ProjectPlanSerialaizers
  #     pg_order_id=request.data.get('pg_order_id')
 #      pg_merchant_id=request.data.get('pg_merchant_id')
       
