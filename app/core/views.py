from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class CustomPageNumberPagination(PageNumberPagination):
    """
        Override the pagination class for dynamic pagination.
        Functionality to dynamically set the page size as a query parameter.
    """

    # Set the name of the query param
    page_size_query_param = 'size'



