# Seguir links (response.follow)

Para ello extremos el xpath del boton next y utilizamos la funcion _follow_ de _response_ con _yield_ la que posee 2 parametros:

```yield response.follow(url, callback=funcion_a_ejecutar_luego_del_response)```

En nuestro caso:

```
next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
if next_page_button_link:
    yield response.follow(next_page_button_link,callback=self.parse)
            ```