from django.contrib import admin
from .models import Category, Client, Machine, Product, Company

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display = ('id', 'name', 'slug')
    list_editable = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email', 'phone')
    list_editable = ('name', 'last_name', 'email', 'phone')
    search_fields = ('name', 'last_name', 'email')
    list_filter = ('last_name',)

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'position', 'model', 'brand', 'status', 'client', 'created_at', 'delivery_in', 'status')
    list_editable = ('ticket', 'position', 'model', 'brand', 'status', 'client', 'delivery_in')
    search_fields = ('ticket', 'model', 'brand', 'client__name', 'client__email')
    list_filter = ('brand', 'status', 'created_at')
    ordering = ('-created_at',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_company', 'phone_company', 'address', 'email', 'nit')
    list_editable = ('name_company', 'phone_company', 'address', 'email', 'nit')
    search_fields = ('name_company', 'phone_company', 'address', 'nit')
    list_filter = ('name_company',)
    ordering = ('name_company',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_editable = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)
