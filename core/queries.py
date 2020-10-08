from core import models
from django.db.models import Q, Case, When, CharField, Value, ExpressionWrapper, F, FloatField, Sum, Count


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


def get_product_by_id_with_or(name):
    queryset = models.Product.objects.filter(created_at__month=2020)
    print(queryset.query)
    return queryset


def get_custom_query():
    queryset = models.Product.objects.annotate(
        status=Case(
            When(price__gte=3000, then=Value('Caro', output_field=CharField())),
            default=Value('Normal', output_field=CharField())
        )
    ).values('id', 'name', 'status')
    return queryset


def gain_percentage():
    queryset = models.Product.objects.annotate(
        gain=ExpressionWrapper(F('price') * Value(0.3), output_field=FloatField())
    ).values('id', 'name', 'price', 'gain')
    return queryset


def query_sum():
    queryset = models.Employee.objects.values(
        'gender'
    ).annotate(
        total=Sum('salary', output_field=FloatField())
    ).values('gender', 'total')

    print(queryset.query)

    return queryset


def query_sum2():
    queryset = models.Employee.objects.aggregate(
        total=Sum('salary', output_field=FloatField())
    )

    return queryset


def total_emplyee_by_departmen():
    queryset = models.Department.objects.values(
        'name',
    ).annotate(
        total=Count('employee__id')
    ).values('name', 'total')
    print(queryset.query)
    return queryset
