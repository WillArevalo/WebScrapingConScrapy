import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'                 # Este es nombre que se llama en terminal
    start_urls = [                  # Direcciones a las que quiero hacerles scraping
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):      #Este metodo define la logica de extraccion
        with open('resultados.html', 'w', encoding='utf-8') as f:
            f.write(response.text)  #El atributo text traer todo lo que descarga scrapy