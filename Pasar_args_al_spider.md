# Pasando Argumentos al Spider

Para obtener no el top ten tags, si no el top tags dinamico que nosotros queramos podemos pasarle argumentos desde la consola al spider para que lo entienda, para ello recurrimos a funciones nativas de python _getattr_ que lo permite es obtener argumentos desde consola.

```top = getattr(self, 'top', None)```

Si existe dentro de la ejecucion de este spider un atributo de nombre top, lo guardare en top si no es None y se pasa todo, en este caso el top 10 e internamente luego de recibir hago un slicing del top

En la consola ya puedo utilizar el nuevo arguemnto -a es de arguments

```scrapy crawl quotes -a top=3```