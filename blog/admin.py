from django.contrib import admin
from blog.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
# username: dklog / password: 225544

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass