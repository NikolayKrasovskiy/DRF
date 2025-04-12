import django_filters
from .models import Advertisement

class AdvertisementFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
