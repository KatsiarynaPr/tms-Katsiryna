from django.contrib import admin

from application.blog.models import Post


@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    pass
