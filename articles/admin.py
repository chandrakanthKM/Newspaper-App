from django.contrib import admin
from .models import Article,comment

class CommentInline(admin.StackedInline):
    model = comment

class ArticleAdmin (admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(comment)

# Register your models here.
