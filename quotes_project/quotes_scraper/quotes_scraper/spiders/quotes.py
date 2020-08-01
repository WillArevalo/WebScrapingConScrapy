import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()
# Next Page Button = //ul[@class="pager"]//li[@class="next"]/a/@href

class QuotesSpider(scrapy.Spider):
    name = 'quotes'             # Estos nombres son los que se invocan y se deben digitar de manera irrepetible dentro del proyecto
    start_urls = [              # La lista de direcciones desde las que comienza el Spider
        'http://quotes.toscrape.com/page/1'
    ]

    custom_settings = {           # Esta configuracion permite ejecutar y guardar automaticamente
        'FEED_URI':'quotes.json',
        'FEED_FORMAT':'json'
    }

    def parse(self, response):  # Este metodo analiza toda la respuesta y trae solo lo que queremos
        
        url         = response.url
        title       = response.xpath('//h1/a/text()').get()
        quotes      = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        topTenTags  = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        
        yield {
            'url':url,
            'title': title,
            'quotes': quotes,
            'top_ten_tags': topTenTags
        }

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)   #Follow recibe 2 params, el link y el callback que es la funcion que se ejecuta luego de entrar a la pagina
