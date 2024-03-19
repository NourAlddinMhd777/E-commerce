#Django | Authentication ( JWT, Login, Register, Profile ) 5/13
from rest_framework import serializers 
from django.contrib.auth.models import User

class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        #يجب ان تكون بنقس هذه الصيغة لكي تكون مطابقة للuser model
        fields = ["first_name","last_name","email","password"]
        #to Customize Previous feilds :
        extra_kwargs={
            "first_name":{"required":True, "allow_blank":False},
            "last_name":{"required":True, "allow_blank":False},
            "email":{"required":True, "allow_blank":False},
            "password":{"required":True, "allow_blank":False,"min_length":8},
        }

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        #يجب ان تكون بنقس هذه الصيغة لكي تكون مطابقة للuser model
        fields = ["first_name","last_name","email","username"]
    
#Django | Authentication ( JWT, Login, Register, Profile ) 5/13 __END
#Django | Authentication ( JWT, Login, Register, Profile ) 6/13 in views.py