from django.contrib import admin
from .models import Author,Article
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    def gender(self):
        if self.gender:
            return '男'
        else:
            return '女'
    gender.short_description = "性别"
    list_display = ['name','age',gender]
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','date','content']