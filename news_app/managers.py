from django.db import models


class News_categories_manager(models.Manager):
    def __add_category(self, list_category):
        objs = [
            self.model(
                category=i["category"],
            )
            for i in list_category
        ]
        # raw_data.save(using=self.db)
        save = self.bulk_create(objs)
        return save

    # metodo para crear registro de un historial
    def add_category(self, category):
        return self.__add_category(category)


class Country_news_manager(models.Manager):
    def __add_country(self, list_country):
        objs = [
            self.model(
                country=i["country"],
            )
            for i in list_country
        ]
        # raw_data.save(using=self.db)
        save = self.bulk_create(objs)
        return save

    # metodo para crear registro de un historial
    def add_country(self, country):
        return self.__add_country(country)


class News_article_manager(models.Manager):
    def __add_article(self, listDictionary, country, category):
        objs = [
            self.model(
                country=country,
                category=category,
                author=i["author"],
                title=i["title"],
                description=i["description"],
                content=i["content"],
                source=i["source"],
                publishedAt=i["publishedAt"],
                url=i["url"],
                urlToImage=i["urlToImage"],
            )
            for i in listDictionary
        ]
        # raw_data.save(using=self.db)
        save = self.bulk_create(objs)

        return save

    # metodo para crear registro de un historial
    def add_article(self, listDictionary, country, category):
        return self.__add_article(listDictionary, country, category)
