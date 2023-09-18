from django.contrib import admin
from .models import Inventory,Product,Rendezvous,Sale,Customer_Service

admin.site.register(Inventory)

class producto(admin.ModelAdmin):
    list_display = ('Nombre', 'Número de serie', 'Gramaje')
    search_fields = ('precio')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Product)

admin.site.register(Rendezvous)

admin.site.register(Sale)

admin.site.register(Customer_Service)
