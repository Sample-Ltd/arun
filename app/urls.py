from django.urls import path
from .views import paginated_numbers

urlpatterns = [
    path('numbers/arun-1234/', paginated_numbers, name='paginated_numbers'),
]
