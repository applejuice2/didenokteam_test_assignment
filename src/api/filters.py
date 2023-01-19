from rest_framework.filters import SearchFilter


class ServiceFilter(SearchFilter):
    search_param = 'service_name'
