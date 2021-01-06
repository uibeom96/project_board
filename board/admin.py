from django.contrib import admin
from board.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author",  "hit_count", "display_avilable")
    list_display_links = ("title", )
    prepopulated_fields = {"slug": ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post")
    list_display_links = ("post", )