from .models import *
from rest_framework import serializers


class LaptopSerializer(serializers.ModelSerializer):
    price_euros = serializers.FloatField(required=False)
    stock_amount = serializers.IntegerField(required=False)

    class Meta:
        model = Laptop
        fields = '__all__'
        read_only_fields = ['company', 'name', 'type', 'inches', 'resolution', 'cpu', 'ram', 'ssd', 'hdd', 'hybrid',
                            'flash_storage', 'gpu', 'op_sys', 'weight']
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 0


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ['total_sales', 'total_items', 'unique_customers']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    review_date = serializers.DateField(required=False)
    review_title = serializers.CharField(required=False)
    review_content = serializers.CharField(required=False)
    laptop_grade = serializers.CharField(required=False)

    class Meta:
        model = Reviews
        fields = "__all__"


class ReviewSerializerPut(serializers.ModelSerializer):
    review_date = serializers.DateField(required=False)
    review_title = serializers.CharField(required=False)
    review_content = serializers.CharField(required=False)
    laptop_grade = serializers.CharField(required=False)

    class Meta:
        model = Reviews
        fields = "__all__"
        read_only_fields = ['customer', 'laptop',]