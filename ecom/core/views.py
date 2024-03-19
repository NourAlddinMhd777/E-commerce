from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateAPIView ,DestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from .filters import productsFilter
from .models import Product,Review
from .serializers import productsSerializers
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Avg
# Create your views here.

# Ecommerce Products Views, Urls 2/3
class Get_all_product(ListCreateAPIView):

    #Django | Serializers (Serializing objects & Deserializing objects 2/2
    queryset = Product.objects.all()
    serializer_class = productsSerializers
    def get(self,request):
        queryset=self.get_queryset()
        
        #Django | Filters, Search, Pagination   4/4  
        filterset= productsFilter(request.GET,queryset=Product.objects.all().order_by('id'))
        count = filterset.qs.count()
        # # onther method to filter:
        # category= request.query_params.get("category")
        # brand= request.query_params.get("brand")
        # ratings= request.query_params.get("ratings")
        # max_price= request.query_params.get("max_price")
        # min_price= request.query_params.get("min_price")

        # search:
        search_name = request.query_params.get('search_name')
        search_cate= request.query_params.get('search_cate')

        # Paginator:
        perpage = request.query_params.get("perpage",default = 2)
        page = request.query_params.get("page",default = 1)
        paginator= Paginator(queryset,per_page=perpage)
        try:
            items=paginator.page(number=page)
        except EmptyPage :
            items=[]
        # # filter step 2:
            
        # if category:
        #     items=queryset.filter(category =category)
        # if brand:
        #     items=queryset.filter(brand=brand)
        # if ratings:
        #     items=queryset.filter(ratings=ratings)
        # if min_price:
        #     items=queryset.filter(price__gte=min_price)
        # if max_price:
        #     items=queryset.filter(price__lte=max_price)
            
        # search step 2:
        if search_name :
            items = queryset.filter(name__icontains=search_name)
        if search_cate :
            items = queryset.filter(category__icontains=search_cate)
        #Django | Filters, Search, Pagination 4/4 __END
        #Django | Filters, Search, Pagination __END
        #next step : Django | Error Exception Handling - 404 500 Errors in general file
            
        serializer_items = self.serializer_class(filterset.qs,many=True)
        return Response({"products":serializer_items.data, "per page":perpage, "count":count},status=status.HTTP_200_OK)
    #Django | Serializers (Serializing objects & Deserializing objects 2/2__END
    #Django | Serializers (Serializing objects & Deserializing objects __END
    #next step : Django | Filters, Search, Pagination 
# Ecommerce Products Views, Urls 2/3__END
# Ecommerce Products Views, Urls 3/3__in urls.py
    
#Django | Filters, Search, Pagination   1/4   
class Get_by_id_product(RetrieveUpdateAPIView,DestroyAPIView):
    # #Django | IsAuthenticated, permissions 3/
    # permission_classes = [IsAuthenticated]
    # #Django | IsAuthenticated, permissions 3/
    # #Django | IsAuthenticated, permissions 4/  in settings.py
    queryset = Product.objects.all()
    serializer_class = productsSerializers
    def get(self,request,id):
        items=get_object_or_404(Product,pk =id)
        serializer_items = self.serializer_class(items)
        return Response(serializer_items.data,status=status.HTTP_200_OK)
#Django | Filters, Search, Pagination   1/4 __END
#Django | Filters, Search, Pagination  2/4 in urls.py     

# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 1/8
@api_view(["POST"])
@permission_classes([IsAuthenticated,IsAdminUser])
def new_product(request):
    data=request.data
    serializer = productsSerializers(data=data)
    if serializer.is_valid():
        product = Product.objects.create(**data,user = request.user)
        res = productsSerializers(product,many = False)
        return Response({"product":res.data},status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)
# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 1/8 __END
# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 2/8  in urls.py

# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 3/8
@api_view(["PUT"])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_product(request,id):
    product = get_object_or_404(Product,id=id)
    if product.user != request.user:
        return Response ( {"error": "sorry,you can't update this product"},status=status.HTTP_403_FORBIDDEN)
    else:
        product.name =  request.data["name"]
        product.discraption =  request.data["discraption"]
        product.price =  request.data["price"]
        product.category =  request.data["category"]
        product.brand =  request.data["brand"]
        product.ratings =  request.data["ratings"]
        product.stock =  request.data["stock"]
        product.save()
        serializer = productsSerializers(product)

        return Response({"product_after_update":serializer.data},status=status.HTTP_200_OK)
# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 3/8 __END
# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 4/8  in urls.py

# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 5/8
@api_view(["DELETE"])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_product(request,id):
    product = get_object_or_404(Product,id=id)
    if product.user != request.user:
        return Response ( {"error": "sorry, you can't update this product"},status=status.HTTP_403_FORBIDDEN)
    else:
        product.delete()
        product.save()

        return Response({"message":"The product has been deleted"},status=status.HTTP_200_OK)

# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 5/8 __END
# Django | IsAuthenticated, permissions (Create, Read, Show, Update & Delete ) 6/8  in urls.py

# Django | Review & Rating API 3/7
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_review(request,pk):
    user = request.user
    product = get_object_or_404(Product,id=pk)
    review =product.review_product.filter(user=user)
    data= request.data
    if data["ratings"] <=0 or data["ratings"] > 10:
        return Response({"error":"please select between 1 to 10"},status=status.HTTP_400_BAD_REQUEST)
    elif review.exists():
        new_review= {"ratings":data["ratings"],"comment":data["comment"]}
        review.update(**new_review)
        
        rating= product.review_product.aggregate(avg_ratings=Avg('ratings'))
        product.ratings = rating['avg_ratings']
        product.save()
        return Response({"details":"Product review updated"})
    else:
        review=Review.objects.create(
            user =user,
            product = product,
            ratings = data['ratings'],
            comment = data['comment']
        )
        rating= product.review_product.aggregate(avg_ratings = Avg('ratings'))
        product.ratings = rating['avg_ratings']
        product.save()
        return Response ({"details":"Product review created"})     
# Django | Review & Rating API 3/7 __END
# Django | Review & Rating API 4/7 in urls.py
    
# Django | Review & Rating API 6/7
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delet_review(request,pk):
    user = request.user
    product = get_object_or_404(Product,id=pk)
    review=product.review_product.filter(user=user) 
    if review.exists() :
        review.delete()
        rating= product.review_product.aggregate(avg_ratings = Avg("ratings"))
        product.ratings = rating['avg_ratings']
        product.save()
        if rating['avg_ratings'] is None:
            rating['avg_ratings']
            product.ratings=rating['avg_ratings']
            product.save()
            return Response({"details":"product review deleted"})
    else:
        return Response({"error":"Review not found"},status=status.HTTP_404_NOT_FOUND)
# Django | Review & Rating API 6/7 __END
# Django | Review & Rating API 7/7 in urls.py
# next step : Django | Email Mailtrap - UserProfile, Forgot Reset Password in views.py/accounts
    