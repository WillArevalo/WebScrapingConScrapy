# Creando el proyecto para extraer citas

1. Creo una carpeta y en la terminal sobre la carpeta escribo:
    ```scrapy startproject quotes_scraper```

    Luego de crear el proyecto al ingresar a la carpeta vemos que existe un archivo _scrapy.cfg_ que contiene configuraciones para el deploy. 
    
    Dentro de la carpeta del proyecto existen diferentes archivos. El archivo _pipelines.py_ es un archivo que nos permite modificar los datos desde que entran a los spiders haste llegar al final.

    _middlewares.py_ es un archivo que nos permite trabajar con un concepto denominado como señales, es decir que podemos controlar eventos que suceden en algun momento de el tiempo en el que se hace la request (peticion), obtenemos la informacion, y la traemos a el programa.

    En _items.py_ encontramos una manera compleja de poder transformar y jugar con los datos que nos envia la respuesta html, para juardarlos de una manera estandar.

    *__ init __.py* es el que determina que el proyecto es un modulo de python

    En la carpeta _spyders_ es en donde se trabaja regularmente
    
    En _settings.py_ encontramos configuraciones de el spider, dentro de este archivo encontramos cosas interesantes como:

    - BOT_NAME: Se define el nombre del robot con el cual se refiere a si mismo en los requests

    - ROBOTSTXT_OBEY: Este parametro bool define si se seguira los lineamientos del website o no.
    - CONCURRET_REQUESTS: Ya que scrapy es asincrono, esto nos permitira saber cuantas peticiones tendremos en simultaneo.
    - DONWLOAD_DELAY: Que tiempo espera Scrapy entre descarga y descarga del resultado de la request, por defecto deja 3 segs
    - CONCURRENT_REQUESTS_PER_IP y CONCURRENT_REQUESTS_PER_DOMAIN, permite configurar peticiones por ip y dominio.
    - COOKIES_ENABLED: avtivar o no cookies
    - DEFAULT_REQUEST_HEADER: Se puede cambiar la cabezera del request
    