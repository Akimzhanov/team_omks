from django.contrib import admin

from apps.travel.models import Travel, TravelImages

class TravelImagesAdmin(admin.TabularInline):
    model = TravelImages
    fields = ['picture']
    max_num = 6

class TravelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'phone_number']
    list_filter = ['price']
    search_fields = ['title']
    inlines = [TravelImagesAdmin]


admin.site.register(Travel, TravelAdmin)