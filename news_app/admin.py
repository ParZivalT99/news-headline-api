from django.contrib import admin
from .models import News_article, Country_news, News_categories


class Article(admin.ModelAdmin):
    list_display = ("id", "title", "source", "publishedAt")
    search_fields = ("id",)
    list_filter = (
        "country",
        "category",
    )


class Category(admin.ModelAdmin):
    list_display = ("id", "category")
    search_fields = ("id",)


admin.site.register(News_article, Article)
admin.site.register(Country_news)
admin.site.register(News_categories, Category)
