from django.contrib import admin
from .models import Orders, StatusCrm, ComentCrm

class Comment(admin.StackedInline):
    model = ComentCrm
    fields = ('coment_text', 'coment_db')
    readonly_fields = ('coment_text',)
    extra = 0


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'o_status', 'o_name', 'o_phone', 'o_date',)
    list_display_links = ('id',)
    search_fields = ('id', 'o_name', 'o_phone', 'o_date',)
    list_filter = ('o_status',)
    list_editable = ('o_status', 'o_name', 'o_phone',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'o_status', 'o_date', 'o_phone', )
    readonly_fields = ('id', 'o_date', 'o_name',)


admin.site.register(Orders, OrdersAdmin)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)
