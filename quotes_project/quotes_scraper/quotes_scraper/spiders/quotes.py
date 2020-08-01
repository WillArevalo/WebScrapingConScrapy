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

    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            new_quotes = response.xpath(
                '//span[@class="text" and @itemprop="text"]/text()'
            ).getall()
            new_url = response.url
            kwargs["quotes"].extend(new_quotes)
            kwargs["urls"].append(new_url)

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs=kwargs)   #Follow recibe 3 params, el link y el callback que es la funcion que se ejecuta luego de entrar a la pagina, con args que le puedo pasar
        else:
            yield kwargs


    def parse(self, response):  # Este metodo analiza toda la respuesta y trae solo lo que queremos
        
        urls            = list()
        urls.append(response.url)
        title           = response.xpath('//h1/a/text()').get()
        quotes          = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        topTags         = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            topTags = topTags[:top]

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(
                next_page_button_link, 
                callback=self.parse_only_quotes, 
                cb_kwargs={
                    'title': title,
                    'top_tags': topTags,
                    'urls':urls,
                    'quotes':quotes
                })   #Follow recibe 3 params, el link y el callback que es la funcion que se ejecuta luego de entrar a la pagina, con args que le puedo pasar
