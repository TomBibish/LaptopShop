from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Laptop(models.Model):
    company = models.ForeignKey(Company, on_delete=models.RESTRICT)
    name = models.CharField(max_length=128, null=False, blank=False)
    type = models.CharField(max_length=128, null=False, blank=False)
    inches = models.FloatField(max_length=6, null=False, blank=False)
    resolution = models.CharField(max_length=128, null=False, blank=False)
    cpu = models.CharField(max_length=128, null=False, blank=False)
    ram = models.IntegerField(null=False, blank=False)
    ssd = models.IntegerField(null=True, blank=True)
    hdd = models.IntegerField(null=True, blank=True)
    hybrid = models.IntegerField(null=True, blank=True)
    flash_storage = models.IntegerField(null=True, blank=True)
    gpu = models.CharField(max_length=128, null=False, blank=False)
    op_sys = models.CharField(max_length=128, null=False, blank=False)
    weight = models.FloatField(max_length=128, null=False, blank=False)
    price_euros = models.FloatField(null=False, blank=False)
    stock_amount = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.name} by {self.company}"


class Customer(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order_date = models.DateField()
    is_cancelled = models.BooleanField(default=False)
    order_laptops = models.ManyToManyField(to=Laptop, through="OrderItem")
    total_price = models.FloatField(null=False, blank=False, default=0)

    def __str__(self):
        return f"Order number {self.pk} by {self.customer}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    laptop = models.ForeignKey(Laptop, on_delete=models.RESTRICT)
    item_price = models.FloatField(null=False, blank=False)
    amount = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.amount} X {self.laptop} for {self.order}"


class Stats(models.Model):
    total_sales = models.FloatField(null=False, blank=False)
    total_items = models.IntegerField(null=False, blank=False)
    unique_customers = models.CharField(max_length=526, null=False, blank=False)


class Reviews(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    laptop = models.ForeignKey(Laptop, on_delete=models.RESTRICT)
    review_date = models.DateField()
    review_title = models.CharField(max_length=128, null=False, blank=False)
    review_content = models.CharField(max_length=526, null=False, blank=False)
    laptop_grade = models.IntegerField( null=False, blank=False)


    def __str__(self):
        return f"Review number {self.pk} by {self.customer} to {self.laptop}"