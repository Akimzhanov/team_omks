from django.contrib import admin
from .models import Brand, Smartphone, SmartImage


# class BrandAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#
#
# class SmartphoneAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}


admin.site.register(Brand)
admin.site.register(Smartphone)
admin.site.register(SmartImage)
