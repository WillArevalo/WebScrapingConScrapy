# Scrapy Shell

Scrapy shell entre otras nos sirve para hacer scraping desde la shell:
_No olvidar el ambiente virtual_

1.  ```scrapy shell 'http://quotes.toscrape.com/page/1'```
2.  ```response.xpath('//h1/a/text()')```                   Esto trae de el texto con tipo de formato
3. ```response.xpath('//h1/a/text()').get()```                Esto trae el texto solo cuando la respuesta es un solo objeto
4. ```response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()```               // sirve para saltar varios niveles, [] dentro se colocan los atributos
5. ```request.method```
6. ```request.encoding```
7. ```response.status```
8. ```response.headers```