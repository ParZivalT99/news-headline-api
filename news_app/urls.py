from django.urls import path, re_path

from . import views

app_name = "news_app"

urlpatterns = [
    path("", views.ArticleListAPIView.as_view()),
    path("category/", views.CategoryListAPIView.as_view(), name="category-list"),
    path("country/", views.CountryListAPIView.as_view(), name="country-list"),
    path("articles/", views.ArticleListAPIView.as_view(), name="article-list"),
    re_path(
        r"^articles/(?P<country_pk>[a-z]{2})/$",
        views.ArticlesByCountryAndCategoryAPIView.as_view(),
        name="article-by-country",
    ),
    re_path(
        r"^articles/(?P<country_pk>[a-z]{2})/(?P<category_pk>[a-z]\w+)/$",
        views.ArticlesByCountryAndCategoryAPIView.as_view(),
        name="article-by-category",
    ),
    path(
        "country/<pk>/",
        views.CountryRetrieveAPIView.as_view(),
        name="country-detail",
    ),
    path(
        "category/<pk>/",
        views.CategoryRetrieveAPIView.as_view(),
        name="category-detail",
    ),
    path(
        "article/<pk>/",
        views.ArticleRetrieveAPIView.as_view(),
        name="article-detail",
    ),
    path(
        "articles/sources/",
        views.ArticleSourcesAPIView.as_view(),
        name="sources-list",
    ),
    re_path(
        r"articles/sources/(?P<country_pk>[a-z]{2})/$",
        views.SourcesByCountryAPIView.as_view(),
        name="sources-by-country",
    ),
]
