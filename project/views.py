import django_filters
from django.db.models import Avg, Sum
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import GenericViewSet,ReadOnlyModelViewSet
#from .filters import CategoriesFilter #BookmarkFilter,CategoriesFilter
from .serializers import ProjectSerializers, CategoriesSerialiser,relationsSerializers
from .models import Project, Categorie,Relations
from rest_framework import mixins, viewsets,permissions



class CategorieViewSet(ReadOnlyModelViewSet):
        serializer_class = CategoriesSerialiser
        queryset = Categorie.objects.all()
        permission_classes = [permissions.IsAuthenticated]


class ProjectListViewSet(mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                             mixins.CreateModelMixin, GenericViewSet):

    serializer_class = ProjectSerializers
    queryset = Project.objects.all().annotate(rate=Avg('relations__rate')).order_by('id').annotate(Sum=Sum('relations__money'))

    #filter_class = CategoriesFilter
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)



class RelationsProfileDetailView(mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                             mixins.CreateModelMixin, GenericViewSet):
    queryset=Relations.objects.all()
    serializer_class=relationsSerializers
    permission_classes=[permissions.IsAuthenticated]


    def get_object(self):
        obj,created=Relations.objects.get_or_create(user=self.request.user,project_id=self.kwargs['project'])

        print('created',created)
        return obj
