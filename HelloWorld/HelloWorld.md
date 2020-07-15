# Como crear un HelloWorld en Scrapy

Lo primero que hago es guardar el html completo, en vez de hacer scraping

Se crea el proyecto desde la terminal con el comnado
```
scrapy startproject NOMBREDELPROYECTO
```

Por lo que ejecuto:
```
scrapy startproject tutorial
```

Luego sigo los pasos que me indica en la terminal

1. Entro a la carpeta creada
2. Creo un archivo en la carpeta spiders siguiendo las buenas practicas, ya que es una pagina de citas(quotes) lo nombro asi _quotes_spider.py_
3. Procedo a configurar el archivo.
4. Ejecuto en terminal 
```
scrapy crawl NOMBREDELSPIDER
```
por lo tanto ejecuto:
```
scrapy crawl quotes
```
5. Da como resultado que sea crea el archivo _resultados.html_ con todo el contenido html que extrajo

_Para scrapear no necesitamos todo el archivo._