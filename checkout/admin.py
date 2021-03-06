from django.contrib import admin
from .models import Order, CrateItems


# Populating crate items model for OrderAdmin
class CrateItemsAdminInline(admin.TabularInline):
    model = CrateItems
    readonly_fields = ('crateitem_total',)
    list_display = ('supply', )


# Order model in admin
class OrderAdmin(admin.ModelAdmin):
    inlines = (CrateItemsAdminInline,)
    readonly_fields = ('date', 'order_number', 'coupon',
                       'order_total', 'original_crate', 'stripe_pid',)

    fields = ('date', 'order_number', 'coupon',
              'user_profile', 'full_name', 'email',
              'contact_number', 'address_line_1', 'address_line_2',
              'town_or_city', 'county', 'postcode', 'country',
              'order_total', 'original_crate', 'stripe_pid',)

    list_display = ('order_number', 'date', 'order_total',
                    'full_name', 'email',)


admin.site.register(Order, OrderAdmin)
