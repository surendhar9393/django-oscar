from django.contrib import admin

from oscar.core.loading import get_model

Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')
PartnerTaxInformation = get_model('customer', 'PartnerTaxInformation')


class PartnerTaxInformationInline(admin.TabularInline):
    model = PartnerTaxInformation
    extra = 0


class StockRecordAdmin(admin.ModelAdmin):
    list_display = ('product', 'partner', 'partner_sku', 'price_excl_tax', 'num_in_stock')
    list_filter = ('partner',)
    

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'users', 'caption', 'product_classes', 'image', 'value_text')
    inlines = [PartnerTaxInformationInline]


admin.site.register(Partner, PartnerAdmin)
admin.site.register(StockRecord, StockRecordAdmin)
