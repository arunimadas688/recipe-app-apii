"""
Core views for app.
"""
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def health_check(request):
    """Returns successful response."""
    return JsonResponse({'healthy': True})