from rest_framework import serializers
from .models import Product,Review

#Django | Serializers (Serializing objects & Deserializing objects 1/2 
#important Note: please don't forget import serializers module
class productsSerializers(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(method_name="get_reviews",read_only =True)
    id =serializers.IntegerField(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id","name","discraption","price","category","brand","ratings","stock","reviews"]

    # Django | Review & Rating API 5/7
    def get_reviews (self,obj):
        reviews=obj.review_product.all()
        serializers = ReviewsSerializers(reviews,many= True)
        return serializers.data
    # Django | Review & Rating API 5/7 __END
    # Django | Review & Rating API 6/7 in views.py 
#Django | Serializers (Serializing objects & Deserializing objects 1/2__END
#Django | Serializers (Serializing objects & Deserializing objects in views.py 2/2
# NOTE : don't forget migrations
        
# Django | Review & Rating API 2/7
class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"      
# Django | Review & Rating API 2/7 __END
# Django | Review & Rating API 3/7 in views.py
# NOTE : don't forget migrations