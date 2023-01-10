from django_filters import rest_framework as filters
from users.models import CustomUser


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class UserFilter(filters.FilterSet):
    user = filters.CharFilter('username')

    class Meta:
        model = CustomUser
        fields = ('username',)