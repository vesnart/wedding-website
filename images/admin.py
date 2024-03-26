from django.contrib import admin
from .models import Image, Contact, TrackingScript, Discount
from django.utils.html import format_html


# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'image_description', 'image_tag', 'larger_image_tag')
    list_filter = ('category',)
    search_fields = ('category', 'image_description')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:auto;" />', obj.image.url)
        return "-"

    def larger_image_tag(self, obj):
        if obj.larger_image:
            return format_html('<img src="{}" style="width: 45px; height:auto;" />', obj.larger_image.url)
        return "-"

    image_tag.short_description = 'Image Preview'
    larger_image_tag.short_description = 'Larger Image Preview'

admin.site.register(Image, ImageAdmin)

# Contact Admin

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'wedding_venue', 'phone_number')
    list_filter = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'message', 'phone_number')


    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Name'

admin.site.register(Contact, ContactAdmin)



@admin.register(TrackingScript)
class TrackingScriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'author')
    list_filter = ('active',)
    search_fields = ('name',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'start_date', 'end_date')
    list_filter = ('active', 'start_date', 'end_date', 'author')
    search_fields = ('title',)