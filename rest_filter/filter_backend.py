from django.db.models import Q

from rest_framework import filters


class BaseFilter(filters.BaseFilterBackend):
    """Base filter class for django rest framework views

    The fields can be mapped to a different filter attribute
    by using the mapped fields dictionary, this way we can filter
    related models.
    """

    class Meta:
        fields = []
        mapped_fields = {}

    def filter_queryset(self, request, qs, view):
        filter_dict = {}
        for field in request.query_params.keys():
            if field not in self.Meta.fields:
                continue

            value = request.query_params.getlist(field)

            # get mapped field if it exists
            # else just use the field name
            if getattr(self.Meta, 'mapped_fields', None):
                field = self.Meta.mapped_fields.get(field, field)

            if isinstance(value, list):
                for val in value:
                    if filter_dict.get(field) is None:
                        filter_dict[field] = Q(**{field: val})
                    else:
                        filter_dict[field] |= Q(**{field: val})
            else:
                filter_dict[field] = Q(**{field: value})

        for field, query in filter_dict.items():
            qs = qs.filter(query)

        return qs

    def _or_filter(self, request, qs):
        or_queries = []
        for field, value in request.query_params.iterlists():
            if field in self.OR_FIELDS:
                if isinstance(value, list):
                    for val in value:
                        or_queries.append(
                            Q(**{field: val})
                        )
                else:
                    or_queries.append(
                        Q(**{field: val})
                    )

        if or_queries:
            or_query = or_queries[0]
            for query in or_queries[1:]:
                or_query |= query
            qs = qs.filter(or_query)

        return qs
