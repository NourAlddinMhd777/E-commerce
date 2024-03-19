#Django | Filters, Search, Pagination   3/4 
#note: dont forget include " 'django_filters' " in setting file
from django_filters import rest_framework as filters
from .models import Product 

class productsFilter(filters.FilterSet):
    # name = filters.CharFilter(lookup_expr = "iexact")
    class Meta:
        model = Product
        fields = ["brand","category","ratings","price"]

#Django | Filters, Search, Pagination   3/4 __END
#Django | Filters, Search, Pagination  4/ in views.py 