# Django | Error Exception Handling - 404 500 Errors 1/3
from django.http import JsonResponse

def handler404(request,exception):
    message =('path not found')
    response = JsonResponse(data={'error':message})
    response.status_code=404
    return response

def handler500( request):
    message = ('internal server error')
    response = JsonResponse(data={'error': message})
    response.status_code = 500
    return response

def handler400(request,exception):
    message =('Bad Request')
    response = JsonResponse(data={'error':message})
    response.status_code=400
    return response
# Django | Error Exception Handling - 404 500 Errors 1/3 __END
# Django | Error Exception Handling - 404 500 Errors 2/3 in ecom/urls.py