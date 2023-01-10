from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Card)
admin.site.register(LabelCard)
admin.site.register(Label)
admin.site.register(Favourites)
admin.site.register(Member)
admin.site.register(CheckList)
admin.site.register(CheckListCard)
admin.site.register(Attachment)
admin.site.register(AttachmentCard)
admin.site.register(LabelColor)
admin.site.register(RecentViews)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'author', 'created_on', 'card']
    list_filter = ['created_on']
