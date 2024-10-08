from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StoreUser(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    role_choices = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=100,choices=role_choices,default='staff')
    user_status_choice = [
        ('active','Active'),
        ('inactive','InActive')
    ]
    user_status = models.CharField(max_length=100,choices=user_status_choice,default='active')
    def __str__(self):
        return str(self.user)

   

class Product(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    unit_of_measure= models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    unit_of_measure_choices = [
        ('ea', 'EA'),
        ('lb','LB'),
        ('box', 'BOX'),
        ('doz', 'DOZ'),
        ('kg','KG'),
        ('m','M'), 
        ('g','G'),
        ('l','L'),
        ('ml','ML'),
        ('gal','GAL'),
    ]
    unit_of_measure = models.CharField(max_length=100,choices=unit_of_measure_choices,default='ea')
    catagorie_choices = [
        ('electronics', 'Electronics'),
        ('clothing','Clothing'),
        ('home and kitchen','Home and Kitchen'),
        ('beauty and personal care','Beauty and Personal Care'),
        ('sports and outdoors','Sports and Outdoors'),
        ('groceries','Groceries'),
        ('toys and games','Toys and Games'),
        ('automotive','Automotive'),
        ('books and media','Books and Media'),
        ('health and wellness',' Health and Wellness'),
        ('office supplies','Office Supplies'),
        ('pet supplies','Pet Supplies'),
        ('automotive','Automotive'),
        ('arts and crafts','Arts and Crafts'),
        ('baby and kids','Baby and Kids'),
        ]
    catagoires = models.CharField(max_length=200,choices=catagorie_choices)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default=product.name)
    total_price  = models.DecimalField(max_digits=10,decimal_places=2)
    amount = models.IntegerField()
    status_choices = [
        ('pending', 'Pending'),
        ('fulfilled', 'Fulfilled'),
        ('canceled', 'canceled'),
    ]
    shipping_address = models.CharField(max_length=300)
    status = models.CharField(max_length=100,choices=status_choices,default='pending')
    
    def __str__(self):
        return self.product.name

class Sale(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    customer_address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class StoreReport(models.Model):
    report_date = models.DateField(auto_now_add=True) # date of this report generated
    low_stock_level_items = models.IntegerField() # number of items with low amount of stock
    sold_items_amount = models.IntegerField() # amount of sold items
    sold_items_price = models.DecimalField(max_digits=10,decimal_places=2) # total price of all sold items 
    order_amount = models.IntegerField() # number of ordered items
    canceled_orders = models.IntegerField() # number of canceled orders
    
    def __str__(self):
        return self.report_date    