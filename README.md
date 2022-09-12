[Read in English](#english-version)
 
# News headline API

Este proyecto consta de una REST API desarrollada en
[Django Rest Framework](https://www.django-rest-framework.org/),
en la cual a través de EndPoints se puede acceder 
a las noticias titulares del momento de Estados 
Unidos y Colombia ofrecidas por la API 
de [NewsAPI](https://newsapi.org/)

> **El proyecto se desarrolló con fines de aprendizaje**
 
## Nota

El proyecto fue construido con base a los datos
que retorna el EndPoint de [Top headlines](https://newsapi.org/docs/endpoints/top-headlines)
ofrecido por [NewsAPI](https://newsapi.org/)

## Requisitos 
El proyecto se construyo usando principalmente lo siguiente:

```
Django==3.2.15
django-cors-headers==3.13.0
djangorestframework==3.13.1
pandas==1.4.3
requests==2.28.1
black==22.6.0
```
# Funcionamiento
Las noticias se dividen en 7 géneros y 2 países:

        Generos: business, entertainment,general,health,science,sports,technology.
        Paises: Colombia (co), Estados Unidos (us)

- Llenar base de datos:
    
    ```
    # Primero hay que hacer las migraciones 
    # luego abrir el shell de django  y escribir lo siguiente:

    >>> from news_data.etl_news import APINews as news
    >>> c=news()

    # guardar en la base de datos las noticias de Estados Unidos
    >>>c.news('us')
    
    # guardar en la base de datos las noticias de Colombia
    >>>c.news('co')
    
    # Ahora ya se puede correr el servidor local para usar la API
    ```
    
Para acceder a los endpoints de la API hay que
crear un usuario en el administrador de Django
o crear un superusuario

- API EndPoints
        
        > requiere usuario autenticado
            - api/v1/
            - api/v1/ category/
            - api/v1/ country/
            - api/v1/ articles/
            - api/v1/ articles/<country_pk>/
            - api/v1/ articles/<country_pk>/<category_pk>/
            - api/v1/ country/<pk>/ 
            - api/v1/ category/<pk>/ 
            - api/v1/ article/<pk>/ 
            - api/v1/ articles/sources/ 
        
        > requiere usuario admin
            - api/v1/ articles/sources/<country_pk>/

# English version

## News headline API

This project consists of a REST API developed in [Django Rest Framework](https://www.django-rest-framework.org/), in which through EndPoints you can access the current headline news from the United States and Colombia offered by the [NewsAPI](https://newsapi.org/) API.

> **The project was developed for learning purposes**
 
## Nota

The project was built based on the data returned by the EndPoint of [Top headlines](https://newsapi.org/docs/endpoints/top-headlines) provided by [NewsAPI](https://newsapi.org/)

## Requirements 
The project was built using mainly the following:
```
Django==3.2.15
django-cors-headers==3.13.0
djangorestframework==3.13.1
pandas==1.4.3
requests==2.28.1
black==22.6.0
```
## How it works
The news are divided into 7 categories and 2 countries:

	Categories: business,entertainment,general,health,science,sports,technology.
	Countries: Colombia (co), United States (us)

- Fill database:
    
    ```
    # First, migrations must be performed
    # then open the django shell and type the following:

    >>> from news_data.etl_news import APINews as news
    >>> c=news()

    # save news from the United States in the database
    >>>c.news('us')
    
    # save news from Colombia in the database
    >>>c.news('co')
    
    # The local server can now be run to use the API
    ```
    
>To access the API endpoints, you need to create a user in the Django admin or create a superuser.

- API EndPoints
        
        > requires authenticated user
            - api/v1/
            - api/v1/ category/
            - api/v1/ country/
            - api/v1/ articles/
            - api/v1/ articles/<country_pk>/
            - api/v1/ articles/<country_pk>/<category_pk>/
            - api/v1/ country/<pk>/ 
            - api/v1/ category/<pk>/ 
            - api/v1/ article/<pk>/ 
            - api/v1/ articles/sources/ 
        
        > requires admin user
            - api/v1/ articles/sources/<country_pk>/
