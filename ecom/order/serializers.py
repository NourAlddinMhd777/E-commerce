from .models import Order
from .models import OrderItem
from rest_framework import serializers


# Django | Order Model, Order Item Model in order application 4/12
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField(method_name="get_oreder_item",read_only=True)
    class Meta:
        model = Order
        fields = "__all__"

    def get_oreder_item(self,obj):
        order_item = obj.orderitems.all()
        serializer = OrderItemSerializer(order_item,many=True)
        return serializer.data
# Django | Order Model, Order Item Model in order application 4/12 __END
# Django | Order Model, Order Item Model in order application 5/12 in views.py
