from core import models


def get_all_products():
    queryset = models.Product.objects.all().order_by('-id')
    print(queryset.query)
    return queryset


def get_all_products_limit_columns():
    queryset = models.Product.objects.all().order_by('-id').values('id', 'name')
    print(queryset.explain())
    print(queryset.query)
    return queryset


def get_product_by_id(name):
    queryset = models.Product.objects.filter(name__icontains=name, active=True)
    print(queryset.query)
    return queryset
