from django.contrib import admin
from .models import  Product, StoreUser,Order, Sale,StoreReport

# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ("id","name","amount","unit_price", "unit_of_measure", "catagoires")

class StoreUserAdmin(admin.ModelAdmin):
    list_display = ("id","user_id", "user" ,"role","user_status")
    def id(self,obj):
        return obj.user.id

class salesAdmin(admin.ModelAdmin):
    list_display = ("id", "name","price","customer_address")


class OrderAdmin(admin.ModelAdmin):
    list_display =  ('product','total_price', 'amount','shipping_address','status')

class ReportModel(admin.ModelAdmin):
    list_display = ('report_date','low_stock_level_items', 'sold_items_amount','sold_items_price','order_amount','canceled_orders')

admin.site.register(StoreUser,StoreUserAdmin)
admin.site.register(Product, productAdmin)
admin.site.register(Sale, salesAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(StoreReport,ReportModel)