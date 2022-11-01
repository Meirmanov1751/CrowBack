from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from example.models import ExampleRelatedModel, Example
from example.serializers import ExampleReadSerializer, ExampleWriteSerializer, ExampleRelatedModelSerializer


class ExampleRelatedModelViewSet(ModelViewSet):
    serializer_class = ExampleRelatedModelSerializer
    queryset = ExampleRelatedModel.objects.all()


class ExampleViewSet(RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = ExampleWriteSerializer
    queryset = Example.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        # SAFE_METHODS это в основном GET и т.д.
        if self.request.method in SAFE_METHODS:
            return ExampleReadSerializer
        return ExampleWriteSerializer
