from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from .models import News_categories, Country_news, News_article
from .serializers import (
    NewsCategoriesSerializer,
    CountryNewsSerializer,
    NewsArticleSerializerLink,
    NewsArtliclePagination,
    NewsArticleSourcesSerializer,
)


class ArticlesByCountryAndCategoryAPIView(ListAPIView):

    serializer_class = NewsArticleSerializerLink
    pagination_class = NewsArtliclePagination
    countries = ["co", "us"]
    categories = [
        "business",
        "entertainment",
        "general",
        "health",
        "science",
        "sports",
        "technology",
    ]

    def get(self, request, *args, category_pk=None, **kwargs):
        country = self.kwargs["country_pk"]

        if country in self.countries:
            if "category_pk" in self.kwargs:
                if self.kwargs["category_pk"] in self.categories:
                    return super(ArticlesByCountryAndCategoryAPIView, self).get(
                        request, *args, **kwargs
                    )
                else:
                    return Response(
                        {"bad request": "Wrong category"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            return super(ArticlesByCountryAndCategoryAPIView, self).get(
                request, *args, **kwargs
            )
        else:
            return Response(
                {"bad request": "Wrong country"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        country = get_object_or_404(Country_news, country=self.kwargs["country_pk"])
        if "category_pk" in self.kwargs:
            category = get_object_or_404(
                News_categories, category=self.kwargs["category_pk"]
            )
            queryset = News_article.objects.filter(country=country, category=category)
        else:
            queryset = News_article.objects.filter(country=country)

        return queryset


class CategoryListAPIView(ListAPIView):

    queryset = News_categories.objects.all()
    serializer_class = NewsCategoriesSerializer


class CountryListAPIView(ListAPIView):

    queryset = Country_news.objects.all()
    serializer_class = CountryNewsSerializer


class ArticleListAPIView(ListAPIView):

    queryset = News_article.objects.all()
    serializer_class = NewsArticleSerializerLink
    pagination_class = NewsArtliclePagination


class CountryRetrieveAPIView(RetrieveAPIView):

    queryset = Country_news.objects.all()
    serializer_class = CountryNewsSerializer


class CategoryRetrieveAPIView(RetrieveAPIView):

    queryset = News_categories.objects.all()
    serializer_class = NewsCategoriesSerializer


class ArticleRetrieveAPIView(RetrieveAPIView):

    queryset = News_article.objects.all()
    serializer_class = NewsArticleSerializerLink


class ArticleSourcesAPIView(ListAPIView):

    queryset = News_article.objects.order_by().values("source").distinct()
    serializer_class = NewsArticleSourcesSerializer
    pagination_class = NewsArtliclePagination


class SourcesByCountryAPIView(ListAPIView):

    permission_classes = (permissions.IsAdminUser,)
    serializer_class = NewsArticleSourcesSerializer
    pagination_class = NewsArtliclePagination

    countries = ["co", "us"]

    def get(self, request, *args, **kwargs):
        country = self.kwargs["country_pk"]

        if country in self.countries:
            return super(SourcesByCountryAPIView, self).get(request, *args, **kwargs)
        else:
            return Response(
                {"bad request": "Wrong country"}, status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        country = get_object_or_404(Country_news, country=self.kwargs["country_pk"])
        queryset = (
            News_article.objects.filter(country=country)
            .order_by()
            .values("source")
            .distinct()
        )

        return queryset
