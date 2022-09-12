from django.db import models

from .managers import (
    News_categories_manager,
    Country_news_manager,
    News_article_manager,
)


class News_categories(models.Model):

    category = models.CharField("Category name", max_length=20, blank=False)

    objects = News_categories_manager()

    class Meta:
        verbose_name = "News Category "
        verbose_name_plural = "News Categories"

    def __str__(self):
        return self.category


class Country_news(models.Model):

    country = models.CharField("country name", max_length=2, blank=False)

    objects = Country_news_manager()

    class Meta:
        verbose_name = "Country News"
        verbose_name_plural = "Countries News"

    def __str__(self):
        return self.country


class News_article(models.Model):

    country = models.ForeignKey(Country_news, on_delete=models.CASCADE)
    category = models.ForeignKey(News_categories, on_delete=models.CASCADE)
    author = models.CharField("Author", max_length=30, blank=False)
    title = models.CharField("Title", max_length=250, blank=False)
    description = models.CharField("Description", max_length=250, blank=False)
    content = models.CharField("Content", max_length=250, blank=False)
    source = models.CharField("Source", max_length=100, blank=False)
    publishedAt = models.CharField("Published at", max_length=30, blank=False)
    url = models.SlugField(max_length=250, blank=False)
    urlToImage = models.SlugField("Image url", max_length=250, blank=False)

    objects = News_article_manager()

    class Meta:
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"
        ordering = ("id",)

    def __str__(self):
        return str(self.id)


""" 
c = Country_news('general')
n = News_categories.objects.add_category('co')
Country_news.objects.add_country('co') 

lista = [
    {
        "source": "Marca",
        "author": "VÍCTOR FRANCH",
        "title": "¡Mojica ficha por el Villarreal! - Marca Colombia",
        "description": "El Villarreal confirmará en las próximas horas el fichaje del lateral colombiano, Johan Mojica. El conjunto amarillo ha llegado a un acuerdo de traspaso con el Elche, por lo que...",
        "url": "https://co.marca.com/claro/futbol/colombianos-mundo/2022/09/01/6310cbecca4741f4198b45af.html",
        "urlToImage": "https://e00-co-marca.uecdn.es/claro/assets/multimedia/imagenes/2022/09/01/16620453303106.jpg",
        "publishedAt": "2022-09-01T15:26:11Z",
        "content": "Mojica controla un balón durante un partido con el Elche\r\nJosé Antonio Sanz\r\nEl Villarreal confirmará en las próximas horas el fichaje del lateral colombiano, Johan Mojica. El conjunto amarillo ha ll… [+2218 chars]",
    },
    {
        "source": "As.com",
        "author": "As.com",
        "title": "Así quedan las clasificaciones tras la etapa 12 de la Vuelta a España - AS ",
        "description": "Richard Carapaz se llevó el triunfo de etapa en Peñas Blancas y Remco Evenepoel mantuvo el maillot de líder ante los ataques de hombres como Mas.",
        "url": "https://as.com/ciclismo/asi-quedan-las-clasificaciones-tras-la-etapa-12-de-la-vuelta-a-espana-n/",
        "urlToImage": "https://img.asmedia.epimg.net/resizer/DA9tWS-gsvGGGuftYK965Dd3Xa4=/644x362/cloudfront-eu-central-1.images.arcpublishing.com/diarioas/NUH4ZV4CVJBZBNHGVJ6QEQNGYI.png",
        "publishedAt": "2022-09-01T15:24:50Z",
        "content": "Richard Carapaz se llevó el triunfo en la 12ª etapa de la Vuelta a España, un nuevo final en alto inédito en el puerto malagueño de Peñas Blancas. El ecuatoriano del Ineos atacó desde la fuga y entró… [+647 chars]",
    },
]
News_article.objects.add_article(lista, Country_news.objects.get(id=1), News_categories.objects.get(id=1)
)
"""
