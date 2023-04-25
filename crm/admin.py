from django.contrib import admin
from .models import CommentCRM, Order, StatusCRM

class Comment(admin.StackedInline):
    model = CommentCRM
    fields = ('comment_dt', 'comment_text', 'comment_binding')
    readonly_fields = ('comment_dt',)
    extra = 0

class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_dt', 'order_name', 'order_phone', 'order_status')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_dt', 'order_name', 'order_phone')
    list_filter = ('order_status',)
    list_editable = ('order_phone', 'order_status')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_dt', 'order_name', 'order_phone', 'order_status')
    readonly_fields = ('id', 'order_dt')
    inlines = [Comment,]

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCRM)
admin.site.register(CommentCRM)
