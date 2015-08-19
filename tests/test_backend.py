import pytest

from rest_filter.filter_backend import BaseFilter

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView

from .models import BasicModel

factory = APIRequestFactory()


class Filter(BaseFilter):
    class Meta:
        fields = [
            'text'
        ]


@pytest.mark.django_db
class TestFilterBackend(object):
    def test_filters(self):
        backend = Filter()
        request = Request(factory.get('/'))
        qs = BasicModel.objects.all()
        view = APIView()
        filtered_qs = backend.filter_queryset(request, qs, view)
        assert qs == filtered_qs

    def test_filters_query(self):
        backend = Filter()
        request = Request(factory.get('/', {'text': 'txt'}))
        qs = BasicModel.objects.all()
        view = APIView()
        filtered_qs = backend.filter_queryset(request, qs, view)
        assert qs.query != filtered_qs.query

    def test_filters_or_query(self):
        backend = Filter()
        request = Request(factory.get('/', {'text': ['txt', 'axt']}))
        qs = BasicModel.objects.all()
        view = APIView()
        filtered_qs = backend.filter_queryset(request, qs, view)
        assert qs.query != filtered_qs.query
        # check or queries exist
        assert len(filtered_qs.query.where.children[0].children) == 2
