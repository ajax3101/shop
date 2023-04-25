from django.contrib import admin
from .models import CommentCRM, Order, StatusCRM


class Comment(admin.StackedInline):
    model = CommentCRM
    fields = ('comment_dt', 'comment_text', 'comment_binding')
    readonly_fields = ('comment_dt',)
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    pass


