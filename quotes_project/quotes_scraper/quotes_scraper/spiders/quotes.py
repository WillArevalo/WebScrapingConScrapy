import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()

class QuotesSpider(scrapy.Spider):
    name = 'quotes'             # Estos nombres son los que se invocan y se deben digitar de manera irrepetible dentro del proyecto
    start_urls = [              # La lista de direcciones desde las que comienza el Spider
        'http://quotes.toscrape.com/page/1'
    ]
    def parse(self, response):  # Este metodo analiza toda la respuesta y trae solo lo que queremos
        
        title       = response.xpath('//h1/a/text()').get()
        quotes      = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        topTenTags  = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        
        yield {
            'title': title,
            'quotes': quotes,
            'top_ten_tags': topTenTags
        }