from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Django | Order Model, Order Item Model in order application 7/12
    path("orders/new/",views.new_order,name="new_order"),
    # Django | Order Model, Order Item Model in order application 7/ __END
    # Django | Order Model, Order Item Model in order application 8/12 in views.py
    #NOTE: url is http://127.0.0.1:8000/api/orders/new/ ,Use the Post method only to create an order for products

    # Django | Order Model, Order Item Model in order application 9/12

    path("orders/",views.orders,name="orders"),
    #NOTE: url is http://127.0.0.1:8000/api/orders/ ,Use the Get method only to get all orders

    path("orders/<int:pk>",views.get_order,name="get_order"),
    #NOTE: url is http://127.0.0.1:8000/api/orders/<id> ,Use the Get method only to get one order

    # Django | Order Model, Order Item Model in order application 9/12 __END
    # Django | Order Model, Order Item Model in order application 10/12 in views.py

    # Django | Order Model, Order Item Model in order application 11/12

    path("orders/<int:pk>/process/",views.process_order,name="process_order"),
    #NOTE: url is http://127.0.0.1:8000/api/orders/<id>/process/,Use the Put method only to update a status order

    path("orders/<int:pk>/delete/",views.delete_order,name="delete_order"),
    #NOTE: url is http://127.0.0.1:8000/api/orders/<id>/delete/ ,Use the Delete method only to Delete order

    # Django | Order Model, Order Item Model in order application 11/12 __END
    # Django | Order Model, Order Item Model in order application 12/12 in views.py




]
