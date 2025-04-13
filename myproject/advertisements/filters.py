import django_filters
from .models import Advertisement

class AdvertisementFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    status = django_filters.ChoiceFilter(choices=Advertisement.STATUS_CHOICES)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
