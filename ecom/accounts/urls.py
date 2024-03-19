from . import views
from django.urls import path

urlpatterns = [
    #Django | Authentication ( JWT, Login, Register, Profile ) 9/13
    path('register/',views.register,name='register'),
    #NOTE: url is http://127.0.0.1:8000/api/register/ ,And use the post method only to send user information for registration
    #Django | Authentication ( JWT, Login, Register, Profile ) 9/13 __END
    #Django | Authentication ( JWT, Login, Register, Profile ) 10/13 in urls.py/ecom 

    #Django | Authentication ( JWT, Login, Register, Profile ) 12/13
    path('userInfo/',views.current_user,name='current_user_info'),
    #NOTE: url is http://127.0.0.1:8000/api/userInfo/ ,and use only get method to display user information
    #Django | Authentication ( JWT, Login, Register, Profile ) 12/13 __END
    #Django | Authentication ( JWT, Login, Register, Profile ) 13/13 __END
    #next step : Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) in views.py/core

    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 8/8
    path('userInfo/update/',views.update_user,name='update_user_info'),
    #NOTE: url is http://127.0.0.1:8000/api/userInfo/update/ ,and use only put method to update user information
    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 8/8 __END
    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) __END
    # next step: Django | Review & Rating API in models.py/core app

    # Django | Email Mailtrap - UserProfile, Forgot Reset Password 6/9
    path("forgot_password/",views.forgot_password,name="forgot_password"),
    #NOTE: url is http://127.0.0.1:8000/api/forgot_password/ ,and use only post method to send token through email for reset password
    # Django | Email Mailtrap - UserProfile, Forgot Reset Password 6/9 __END
    # Django | Email Mailtrap - UserProfile, Forgot Reset Password 7/9 in models.py

    # Django | Email Mailtrap - UserProfile, Forgot Reset Password 9/9    
    path("reset_password/<str:token>",views.reset_password,name="reset_password"),
    #NOTE: url is http://127.0.0.1:8000/api/forgot_password/ ,and use only post method to reset password
    # Django | Email Mailtrap - UserProfile, Forgot Reset Password 9/9 __END    
    # Django | Email Mailtrap - UserProfile, Forgot Reset Password __END 
    # next step : Django | Order Model, Order Item Model in order application
    # NOTE: create new applicatin called 'order'.

]