from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

# Django | Email Mailtrap - UserProfile, Forgot Reset Password 2/9
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    reset_password_expire = models.DateTimeField(null=True,blank=True)
    reset_password_token=models.CharField(max_length=50,default="",blank=True)
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 2/9 __END
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 3/9 in views.py

# Django | Email Mailtrap - UserProfile, Forgot Reset Password 7/9
@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    # print('instance',instance)
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 7/9 __END
# Django | Email Mailtrap - UserProfile, Forgot Reset Password 8/9 in views.py
