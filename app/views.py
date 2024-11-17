from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination


# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse

@api_view(['GET'])
def paginated_numbers(request):
    # List of numbers from 1 to 50
    numbers = list(range(1, 50))
    
    # Initialize the paginator
    paginator = PageNumberPagination()
    paginator.page_size = 5  # Set the page size (how many numbers per page)
    
    # Paginate the numbers
    paginated_numbers = paginator.paginate_queryset(numbers, request)
    
    # Construct the custom response
    response_data = {
        'count': len(numbers),  # Total number of items
        'next': paginator.get_next_link(),  # URL for the next page
        'previous': paginator.get_previous_link(),  # URL for the previous page
        'results': paginated_numbers  # The actual paginated data
    }
    
    # Return a JsonResponse with the paginated data
    return JsonResponse(response_data)