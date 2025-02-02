from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, ContactMessage


# Register model posts.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'author', 'created_on', 'updated_on')
    search_fields = ['title']
    list_filter = ('status',)


# Register comments model.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'get_status_display',
                    'created_on', 'updated_on')
    readonly_fields = ['content']  # Make content read-only

    def get_status_display(self, obj):
        return obj.get_approved_display()

    get_status_display.short_description = 'Status'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
