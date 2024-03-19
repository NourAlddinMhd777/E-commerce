"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include("core.urls")),

    #Django | Authentication ( JWT, Login, Register, Profile ) 8/13
    path('api/',include("accounts.urls")),
    #Django | Authentication ( JWT, Login, Register, Profile ) 8/13 __END
    #Django | Authentication ( JWT, Login, Register, Profile ) 9/13 in urls.py/accounts

    #Django | Authentication ( JWT, Login, Register, Profile ) 10/13
    path('api/token/',TokenObtainPairView.as_view()),
    #Django | Authentication ( JWT, Login, Register, Profile ) 10/13 __END
    #Django | Authentication ( JWT, Login, Register, Profile ) 11/13 in views.py/accounts
   
   # Django | Order Model, Order Item Model in order application 6/12
    path('api/',include("order.urls")),
   # Django | Order Model, Order Item Model in order application 6/12 __END
   # Django | Order Model, Order Item Model in order application 7/12 in urls.py/order application
]

# # Django | Error Exception Handling - 404 500 Errors 2/3
handler404 = 'utils.error_views.handler404'
handler500 = 'utils.error_views.handler500'
handler400 = 'utils.error_views.handler400'
# # Django | Error Exception Handling - 404 500 Errors 2/3 __END
# # Django | Error Exception Handling - 404 500 Errors 3/3 in settings.py
