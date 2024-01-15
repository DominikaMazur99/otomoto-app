from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Car

class PriceRangeFilter(admin.SimpleListFilter):
    title = _('Price Range')
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return [
            ('0-10000', _('0 - 10,000')),
            ('10001-30000', _('10,001 - 30,000')),
            ('30001-50000', _('30,001 - 50,000')),
            ('50001-70000', _('50,001 - 70,000')),
            ('70001-90000', _('70,001 - 90,000')),
            ('90001-110000', _('90,001 - 110,000')),
            ('110001-150000', _('110,001 - 150,000')),
            ('150001-200000', _('150,001 - 200,000')),
            ('250001-300000', _('250,001 - 300,000')),
            # Add more ranges as needed
        ]

    def queryset(self, request, queryset):
        if self.value():
            min_price, max_price = map(float, self.value().split('-'))
            return queryset.filter(price__gte=min_price, price__lte=max_price)
        return queryset

class MileageRangeFilter(admin.SimpleListFilter):
    title = _('Mileage Range')
    parameter_name = 'mileage_range'

    def lookups(self, request, model_admin):
        return [
                ('0-10', _('0 - 10')),
                ('11-30', _('11 - 30')),
                ('31-50', _('31 - 50')),
                ('51-70', _('51 - 70')),
                ('71-90', _('71 - 90')),
                ('91-110', _('91 - 110')),
                ('111-150', _('111 - 150')),
                ('151-200', _('151 - 200')),
                ('201-250', _('201 - 250')),
            # we can add more range if we want
        ]

    def queryset(self, request, queryset):
        if self.value():
            min_price, max_price = map(float, self.value().split('-'))
            return queryset.filter(mileage__gte=min_price, mileage__lte=max_price)
        return queryset

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'brand', 'fuel_type', 'mileage', 'price', 'year')
    list_filter = (PriceRangeFilter, MileageRangeFilter, 'fuel_type', 'brand', 'year')  #filters in panel on right
    search_fields = ('car_name', 'brand')

admin.site.register(Car, CarAdmin)
