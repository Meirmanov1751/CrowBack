import requests
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .serializers import CommentSerialiser,CommentRelSerialiser
# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets,permissions
from .models import Comment,CommentRelasions



class CommentViewset(mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                           mixins.CreateModelMixin,GenericViewSet):
    serializer_class = CommentSerialiser
    queryset = Comment.objects.all()
    permission_classes =[permissions.BasePermission]








class CommentRelViewset(mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                           mixins.CreateModelMixin,GenericViewSet):
    serializer_class = CommentRelSerialiser
    queryset = CommentRelasions.objects.all()
    permission_classes =[permissions.BasePermission]









