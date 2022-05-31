from django_filters import FilterSet, DateFilter
from .models import Post
from django.forms import DateInput


class PostFilter(FilterSet):
    dateCreation = DateFilter(
        lookup_expr='gt',
        widget=DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    class Meta:
        model = Post
        fields = {'title': ['icontains'],
                  'postCategory': ['exact'],
                  'author': ['exact']
                  }
