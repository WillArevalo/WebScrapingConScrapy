# Guardando datos

Al extraer los datos podemos guardarlos en diferentes formatos para luego ser consumidos por otras aplicaciones y/o personas, en formatos populares como son _CSV_ o _JSON_.

A traves de yield (un retorno parcial) estaremos ingresando los datos a un archivo, por lo que regresamos un diccionario.

la bandera _-o_ refiere a output, va seguido del nombre de archivo de salida con su debida extension sea CSV o JSON

Y en consola ejecutamos ```scrapy crawl quotes -o quotes.json``` o ```scrapy crawl quotes -o quotes.csv```

Si vuelvo a ejecutar algunos de estos comandos lo que se hace es un append, o una insercion nueva, de ser que quiera un archivo desde cero basta con borrar el existente