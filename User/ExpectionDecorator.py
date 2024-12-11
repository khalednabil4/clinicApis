from functools import wraps
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

def handle_api_exception(error_message="An unexpected error occurred.", code=500):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except NotFound as e:
                # Handle NotFound error, specifically for cases like object not found
                return Response({
                    "success": False,
                    "error": error_message,
                    "details": str(e)  # Pass the NotFound exception message
                }, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                # Catch any other exceptions
                print(e)
                return Response({
                    "success": False,
                    "error": error_message,
                    "details": str(e)  # Include the exception details here
                }, status=code)
        return wrapper
    return decorator
