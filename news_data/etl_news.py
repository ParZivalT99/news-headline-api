import json
import requests
from collections import Counter

import pandas as pd

from news_app.models import News_categories, Country_news, News_article


class APINews:
    def __init__(self):
        try:
            with open("secret.json") as s:
                self.api_url = json.loads(s.read())["NEWS_API"]
        except Exception as e:
            raise e

    def connAPI(self, country: str = "co", category: str = "general") -> pd.DataFrame:
        """
        :country: The 2-letter ISO 3166-1 code of the country you want to get headlines for. Possible options:
        us,co, Default: co.

        :category: The category you want to get headlines for. Possible options: business, entertainment,general,health,science,sports,technology. Default: general

        :return: pandas DataFrame
        """

        # /v2/top-headlines
        response = requests.get(
            self.api_url,
            params={"category": category, "country": country, "pageSize": "100"},
        )

        articles = response.json()["articles"]

        df = pd.DataFrame(
            articles,
            columns=[
                "source",
                "author",
                "title",
                "description",
                "url",
                "urlToImage",
                "publishedAt",
                "content",
            ],
        )
        df = df.sort_values(by="publishedAt", ascending=False, ignore_index=True)

        return df

    def dataCleaning(self, df: pd.DataFrame):
        """

        :df:DataFrame of all news
        return: List
        """

        # removing the rows with Nan values from the given columns and reseting their index
        df.dropna(
            subset=[
                "content",
                "description",
                "publishedAt",
                "source",
                "title",
                "url",
                "urlToImage",
            ],
            inplace=True,
        )
        df = df.reset_index().drop(["index"], axis=1)

        # removing the dict and leaving the name of the source
        df.loc[df["source"].index, "source"] = df["source"].str.get("name")

        # if the author is None then get the value of column source
        author_index = df[~df.author.notnull()]["author"].index
        df.loc[author_index, "author"] = df[~df.author.notnull()]["source"]

        # dataFrame to list of dictionaries
        dic = list(json.loads(df.T.to_json()).values())

        # check for duplicate data in the request
        repeated_title = []
        not_repeated = []
        only_title = []

        rep = dict(Counter([i["title"] for i in dic]))

        for i, v in rep.items():
            if v >= 2:
                repeated_title.append(i)

        if not repeated_title:  # if is empty
            return dic
        else:
            for i in range(len(dic)):

                if dic[i]["title"] in repeated_title:
                    if dic[i]["title"] not in only_title:
                        only_title.append(dic[i]["title"])
                        not_repeated.append(dic[i])
                else:
                    not_repeated.append(dic[i])
            return not_repeated

    def insertFilter(
        self,
        listdic_items: list,
        Model,
        field_name: str,
        country="co",
        category="general",
    ):
        """
        :listdic_items:List of dictionaries,  must contain the data to be inserted in the database.

        :Model: Model object in which you want to insert data, available options are ``News_categories`` ``Country_news``,``News_article``.

        :field_name: available options are: ``country``,``category``,``title``.

        :Note: country and category are ``only used when field_name is the 'title'``

        :country: The 2-letter ISO 3166-1 code of the country you want to get headlines for. Possible options:
        us,co. Default: co

        :category: The category you want to get headlines for. Possible options: business, entertainment,general,health,science,sports,technology. Default: general


        """

        if field_name == "country":
            queryset = Model.objects.filter(
                country__in=[t[field_name] for t in listdic_items]
            ).values(field_name)

            insert = Model.objects.add_country

        elif field_name == "category":
            queryset = Model.objects.filter(
                category__in=[t[field_name] for t in listdic_items]
            ).values(field_name)

            insert = Model.objects.add_category

        elif field_name == "title":

            category = News_categories.objects.get(category=category)
            country = Country_news.objects.get(country=country)

            queryset = Model.objects.filter(
                country__exact=country, title__in=[t[field_name] for t in listdic_items]
            ).values(field_name)

            insert = Model.objects.add_article

        if Model.objects.last():
            queryset = [i[field_name] for i in queryset]

            no_duplicates = []

            for i in listdic_items:
                if i[field_name] not in queryset:

                    # data not repeated
                    no_duplicates.append(i)

            if len(no_duplicates) == 0:
                print("there is no new data: ", field_name, " - ", category)
            else:
                print("inserted data: ", len(no_duplicates))

                if field_name == "title":
                    insert(listdic_items, country, category)
                else:
                    insert(no_duplicates)
                print("successful insert!: ", field_name, " - ", category)

        else:
            # print("the database is empty")
            if field_name == "title":
                insert(listdic_items, country, category)

            else:
                insert(listdic_items)
            print("successful insert!:", field_name, " - ", category)

    def news(self, country: str = "co"):
        """
        :country: The 2-letter ISO 3166-1 code of the country you want to get headlines for. Possible options:
        co,us. Default: co
        """
        countries = [{"country": "co"}, {"country": "us"}]

        categories = [
            {"category": "general"},
            {"category": "sports"},
            {"category": "health"},
            {"category": "science"},
            {"category": "technology"},
        ]

        # country
        self.insertFilter(
            listdic_items=countries, Model=Country_news, field_name="country"
        )

        # category
        self.insertFilter(
            listdic_items=categories, Model=News_categories, field_name="category"
        )

        # articles
        for i in categories:
            df = self.connAPI(country=country, category=i["category"])
            df = self.dataCleaning(df=df)
            self.insertFilter(
                listdic_items=df,
                Model=News_article,
                field_name="title",
                country=country,
                category=i["category"],
            )