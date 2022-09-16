import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='Name')
    note = django_filters.NumberFilter(lookup_expr='icontains', label='Note')

    class Meta:
        model = Student
        fields = '__all__'