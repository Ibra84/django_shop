from django.contrib import admin

from orders.models import Order, OrderItem

class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'name', 'price', 'quantity')
    search_fields = ('product', 'name')
    extra = 0
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'name', 'price', 'quantity']
    search_fields = ['order', 'product', 'name']
    
    
class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = [
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_stamp',
    ]   
    
    search_fields = [
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_stamp',
    ] 
    readonly_fields = ['created_stamp',]
    extra = 0
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_stamp',
    )   
    
    search_fields =(
        'id',
    ) 
    
    readonly_fields = ['created_stamp',]
    
    list_filter = [
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_stamp',
    ]
    
    inlines = (OrderItemTabularInline,)
        