from rest_framework import serializers, pagination

from .models import News_categories, Country_news, News_article


class NewsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_categories
        fields = "__all__"


class CountryNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country_news
        fields = "__all__"


class NewsArticleSerializerLink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News_article
        fields = [
            "id",
            "country",
            "category",
            "author",
            "title",
            "description",
            "content",
            "source",
            "publishedAt",
            "url",
            "urlToImage",
        ]

        extra_kwargs = {
            "country": {"view_name": "news_app:country-detail", "lookup_field": "pk"},
            "category": {"view_name": "news_app:category-detail", "lookup_field": "pk"},
        }


class NewsArticleSourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_article
        fields = ["source"]


class NewsArtliclePagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 10
