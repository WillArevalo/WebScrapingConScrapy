# Usando XPath

1. Procedo a configurar, en si tengo estas expresiones en XPath para extraer lo siguiente:
    - Titulo = //h1/a/text()
    - Citas = //span[@class="text" and @itemprop="text"]/text()
    - Top ten tags = //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()