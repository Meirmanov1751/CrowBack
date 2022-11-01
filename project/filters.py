""" import django_filters
from django_filters import filters, DateFilter
from .models import Project
from rest_framework.django_filters.filters import GlobalFilter

class GlobalCharFilter(GlobalFilter, filters.CharFilter):
    pass



class CategoriesFilter(django_filters.FilterSet):
    categories = filters.CharFilter(method='get_categories')

    def get_categories(self, queryset, name, value):
        value = value.split(',')
        if not value:
            return queryset
        return queryset.filter(categories__in=value)

    class Meta:
        model = Project
        fields = ['categories'] """
