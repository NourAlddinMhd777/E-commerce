from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    # Ecommerce Products Views, Urls 3/3
    # Ecommerce Products Views, Urls 3/3__END
    path('products/',views.Get_all_product.as_view(),name="product"),
    #NOTE: url is http://127.0.0.1:8000/api/products ,and use only get method to display products
    # Ecommerce Products Views, Urls END
    #next step : Django | Serializers (Serializing objects & Deserializing objects)  in core file


    #Django | Filters, Search, Pagination   2/4 
    path('products/<int:id>',views.Get_by_id_product.as_view(),name="single_product"),
    #NOTE: url is http://127.0.0.1:8000/api/products/<id> ,and use only get method to display one product by id
    #Django | Filters, Search, Pagination   2/4 __END
    #Django | Filters, Search, Pagination  3/ in filters.py 

    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 2/8
    path('prodcts/new',views.new_product,name="add_new_product"),
    #NOTE: url is http://127.0.0.1:8000/api/products/new ,and use only post method to create a new product
    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 2/8 __END
    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 3/8 in views.py

    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 4/8
    path('products/<int:id>/update',views.update_product,name="update_product"),
    #NOTE: url is http://127.0.0.1:8000/api/products/<id>/update ,and use only put method to update a product by id
    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 4/8 __END
    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 5/8 in views.py

    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 6/8
    path('products/<int:id>/delete',views.delete_product,name="delete_product"),
    #NOTE: url is http://127.0.0.1:8000/api/products/<id>/delete ,and use only delete method to delete a product by id
    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 6/8 __END
    # Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 7/8 in views.py/accounts app


    # Django | Review & Rating API 4/7
    path('products/<int:pk>/review',views.create_review,name="review_product"),
    #NOTE: url is http://127.0.0.1:8000/api/products/<id>/review ,and use only post method to review a product
    # Django | Review & Rating API 4/7 __END
    # Django | Review & Rating API 5/7 in serializers.py

    # Django | Review & Rating API 7/7
    path('products/<int:pk>/review/delete',views.delet_review,name="delete_review_product"),
    #NOTE: url is http://127.0.0.1:8000/api/products/<id>/review/delete ,and use only delete method to delete review a product
    # Django | Review & Rating API 7/7 __END
    # Django | Review & Rating API __END

]
