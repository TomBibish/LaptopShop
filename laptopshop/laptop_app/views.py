import datetime

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import LaptopSerializer, OrderSerializer, StatsSerializer, CompanySerializer, ReviewSerializer, \
    ReviewSerializerPut


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def reviews(request):
    if request.method == 'GET':
        all_reviews = Reviews.objects.all()
        serializer = ReviewSerializer(all_reviews, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            laptop = serializer.validated_data["laptop"]
            customer = serializer.validated_data["customer"]
            all_ordered_laptops_by_laptop = OrderItem.objects.filter(laptop=laptop)
            all_orders_by_cust = Order.objects.filter(customer=customer)
            for ordered_laptop in all_ordered_laptops_by_laptop:
                if ordered_laptop.order in all_orders_by_cust:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return HttpResponse("Can not review a laptop that the customer never bought")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def review_details(request, pk):
    try:
        review = Reviews.objects.get(pk=pk)
    except review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializerPut(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializerPut(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def reviews_for_laptops(request, laptop_id):
    try:
        review = Reviews.objects.get(laptop=laptop_id)
    except review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def laptops(request):
    if request.method == 'GET':
        all_laptops = Laptop.objects.all()
        if 'name' in request.GET and request.GET['name']:
            all_laptops = all_laptops.filter(name__icontains=request.GET['name'])
        if 'resolution' in request.GET and request.GET['resolution']:
            all_laptops = all_laptops.filter(resolution__icontains=request.GET['resolution'])
        if 'sort_by_price' in request.GET:
            if request.GET['sort_by_reviews'] == "desc":
                all_laptops = Laptop.objects.order_by('-price_euros')
            elif request.GET['sort_by_reviews'] == "asc":
                all_laptops = Laptop.objects.order_by('price_euros')
        if 'sort_by_ram' in request.GET:
            if request.GET['sort_by_ram'] == "desc":
                all_laptops = Laptop.objects.order_by('-ram')
            elif request.GET['sort_by_ram'] == "asc":
                all_laptops = Laptop.objects.order_by('ram')
        if 'sort_by_weight' in request.GET:
            if request.GET['sort_by_weight'] == "desc":
                all_laptops = Laptop.objects.order_by('-weight')
            elif request.GET['sort_by_weight'] == "asc":
                all_laptops = Laptop.objects.order_by('weight')
        if 'is_in_stock' in request.GET:
            if request.GET['is_in_stock'] == "True":
                all_laptops = Laptop.objects.filter(stock_amount__gte=1)
            elif request.GET['is_in_stock'] == "False":
                all_laptops = Laptop.objects.filter(stock_amount__lte=0)
        if 'ram_maximum' in request.GET and request.GET['ram_maximum']:
            all_laptops = Laptop.objects.filter(ram__lte=request.GET['ram_maximum'])
        if 'ram_minimum' in request.GET and request.GET['ram_minimum']:
            all_laptops = Laptop.objects.filter(ram__gte=request.GET['ram_minimum'])
        if 'has_ssd' in request.GET:
            if request.GET['has_ssd']:
                all_laptops = Laptop.objects.filter(ssd__gte=1)
            if request.GET['has_ssd'] == "False":
                all_laptops = Laptop.objects.filter(ssd__isnull=True)

        serializer = LaptopSerializer(all_laptops, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LaptopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def laptop_details(request, pk):
    try:
        laptop = Laptop.objects.get(pk=pk)
    except laptop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LaptopSerializer(laptop)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaptopSerializer(laptop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def orders(request):
    if request.method == 'GET':
        all_orders = Order.objects.all()
        if 'customer' in request.GET and request.GET['customer']:
            all_orders = all_orders.filter(customer__name__icontains=request.GET['customer'])
        if 'price_max' in request.GET and request.GET['price_max']:
            all_orders = all_orders.filter(total_price__lte=request.GET['price_max'])
        if 'price_min' in request.GET and request.GET['price_min']:
            all_orders = all_orders.filter(total_price__gte=request.GET['price_min'])
        if 'date_max' in request.GET and request.GET['date_max']:
            all_orders = all_orders.filter(order_date__lte=request.GET['date_max'])
        if 'date_min' in request.GET and request.GET['date_min']:
            all_orders = all_orders.filter(order_date__gte=request.GET['date_min'])
        serializer = OrderSerializer(all_orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        total_price = 0
        customer = request.data['customer']
        order_items = request.data['order_items']
        new_order = Order(customer_id=customer, order_date=datetime.date.today())
        new_order.save()

        for item in order_items:
            laptop = Laptop.objects.get(id=item['laptop'])
            total_price = total_price + (laptop.price_euros * item['amount'])
            order_item = OrderItem(order=new_order,
                                   laptop=laptop,
                                   item_price=laptop.price_euros,
                                   amount=item['amount'])
            if item['amount'] > laptop.stock_amount:
                return HttpResponse("Can't order more then the exist stock amount")
            else:
                laptop.stock_amount = laptop.stock_amount - item['amount']
                laptop.save()
                order_item.save()
        new_order.total_price = total_price
        new_order.save()
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def order_details(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def best_5_laptops(request):
    if request.method == 'GET':
        laptops_count = {}
        all_ordered_items = OrderItem.objects.all()
        for item in all_ordered_items:
            if item.laptop.id in laptops_count:
                laptops_count[item.laptop.id] = laptops_count[item.laptop.id] + item.amount
            else:
                laptops_count[item.laptop.id] = item.amount
        all_laptops = Laptop.objects.all()
        laptops_count = sorted(laptops_count.items(), key=lambda x: x[1], reverse=True)
        laptops_count = dict(laptops_count)
        laptops_ids = [id for id in laptops_count.keys()]
        best_5 = []
        for i in range(4):
            try:
                best_5.append(laptops_ids[i])
            except:
                break
        top_5_laptops = all_laptops.filter(id__in=best_5)
        serializer = LaptopSerializer(top_5_laptops, many=True)
        return Response(serializer.data)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def total_sales_by_date(request, first_date, end_date):
    if request.method == 'GET':
        unique_customers = []
        total_sales = 0
        total_items = 0
        first_date = datetime.datetime.strptime(first_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        all_orders = Order.objects.all()
        all_orders = all_orders.filter(order_date__gte=first_date)
        all_orders = all_orders.filter(order_date__lte=end_date)
        for order in all_orders:
            if order.customer.name not in unique_customers:
                unique_customers.append(order.customer.name)
            total_sales = total_sales + order.total_price
            order_items = OrderItem.objects.filter(order=order)
            for item in order_items:
                total_items = total_items + item.amount
        new_stats = Stats(total_sales=total_sales, total_items=total_items, unique_customers=unique_customers)
        serializer = StatsSerializer(new_stats)
        return Response(serializer.data)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def best_companies(request):
    companies_dict = {}
    new_stats_list = {}
    index = 1
    all_items = OrderItem.objects.all()
    for item in all_items:
        if item.laptop.company.name not in companies_dict.keys():
            companies_dict[item.laptop.company.name] = {'items_count': item.amount,
                                                        'sum_count': (item.amount * item.laptop.price_euros)}
        else:
            companies_dict[item.laptop.company.name]['items_count'] += item.amount
            companies_dict[item.laptop.company.name]['sum_count'] += (item.amount * item.laptop.price_euros)
    return Response(companies_dict)
