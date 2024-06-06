from django.contrib import admin
from blog.models import Category, Comment, Post, Tag
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)