import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'             # Estos nombres son los que se invocan y se deben digitar de manera irrepetible dentro del proyecto
    start_urls = [              # La lista de direcciones desde las que comienza el Spider
        'http://quotes.toscrape.com/page/1'
    ]
    def parse(self, response):  # Este metodo analiza toda la respuesta y trae solo lo que queremos
        print('*'*10, end='\n')
        print(response.status, response.headers)
        print('*'*10, end='\n')