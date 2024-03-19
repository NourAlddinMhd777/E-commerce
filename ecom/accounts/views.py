from datetime import datetime, timedelta
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail



# to password Customize:
from django.contrib.auth.hashers import make_password
# ======================================================
from rest_framework import status
from .serializers import SignUpSerializers,UserSerializers
# Create your views here.

#Django | Authentication ( JWT, Login, Register, Profile ) 6/13
@api_view(["POST"])
def register (request):
    if request.method == "POST":
        data = request.data
        user = SignUpSerializers(data=data)
        if user.is_valid():
            if not User.objects.filter(username = data["email"]).exists():
                user = User.objects.create(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    username=data['email'],
                    email=data["email"],
                    password= make_password(data["password"]),
                )
                return Response(
                    {"details":"your account registered susccessfully!!"},
                    status=status.HTTP_201_CREATED           
                    )
            else:
                return Response(
                    {"Error":"This email already exists!"},
                    status=status.HTTP_400_BAD_REQUEST         
                    )
        else:
            return Response ( user.errors)       
#Django | Authentication ( JWT, Login, Register, Profile ) 6/13 __END
#Django | Authentication ( JWT, Login, Register, Profile ) 7/13 in accounts application file : 
    # create a new python file called : urls
#Django | Authentication ( JWT, Login, Register, Profile ) 8/13 in ecom project file : 
    # include urls.py/accounts inside urls.py/ecom
        

#Django | Authentication ( JWT, Login, Register, Profile ) 11/13
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializers(request.user)
    return Response(user.data)
#Django | Authentication ( JWT, Login, Register, Profile ) 11/13 __END
#Django | Authentication ( JWT, Login, Register, Profile ) 12/13 in urls.py/accounts 

# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 7/8
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data
    user.first_name =data["first_name"]
    user.last_name=data["last_name"]
    user.email=data["email"]
    user.username=data["email"]
    if data["password"] != "":
        user.password=make_password(data["password"])
    user.save()
    serializer = UserSerializers(user)
    return Response(serializer.data,status=status.HTTP_200_OK)
# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 7/8 __END
# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 8/8 in urls.py.py

# Django | Email Mailtrap - UserProfile, Forgot Reset Password 4/9 
def get_current_host(request):
    protocol = request.is_secure() and "https" or "http"
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol,host=host)
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 4/9 __END
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 5/9 in views.py

# Django | Email Mailtrap - UserProfile, Forgot Reset Password 1/9
@api_view(["POST"])
def forgot_password (request):
    data = request.data
    user =get_object_or_404(User,email=data["email"])
    token =get_random_string(40) 
    exprire_date=datetime.now()+timedelta(minutes=30)
 
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 1/9 __END
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 2/9 in models.py
    
    # Django | Email Mailtrap - UserProfile, Forgot Reset Password 3/9
    user.profile.reset_password_token=token
    user.profile.reset_password_expire=exprire_date

    user.profile.save()
    host=get_current_host(request)
    link = "{host}api/reset_password/{token}".format(host=host,token=token)
    # link = "https://localhost:8000/api/reset_password/token"
    body = "Your password reset link is : {link}".format(link=link)
    # Django | Email Mailtrap - UserProfile, Forgot Reset Password 3/9 __END
    # Django | Email Mailtrap - UserProfile, Forgot Reset Password 4/9 in views.py

    # Django | Email Mailtrap - UserProfile, Forgot Reset Password 5/9 
    send_mail(
        "Paswword reset from eMarket",
        body,
        "eMarket@gmail.com",
        [data['email']]
    )
    # print("exprire_date",user.profile.reset_password_expire.replace(tzinfo=None))
    # print("exprire_date",user.profile.reset_password_expire)
    return Response({'details': 'Password reset sent to {email}'.format(email=data['email'])})
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 5/9 __END
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 6/9 in .py

# Django | Email Mailtrap - UserProfile, Forgot Reset Password 8/9 
@api_view(['POST'])
def reset_password(request,token):
    data = request.data
    user = get_object_or_404(User,profile__reset_password_token = token)
    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
        return Response({'error': 'Token is expired'},status=status.HTTP_400_BAD_REQUEST)
    
    if data['password'] != data['confirmPassword']:
        return Response({'error': 'Password are not same'},status=status.HTTP_400_BAD_REQUEST)
    
    user.password = make_password(data['password'])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None 
    user.profile.save() 
    user.save()
    return Response({'details': 'Password reset done '})
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 8/9 __END
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 9/9 in urls.py
