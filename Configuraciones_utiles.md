# Configuraciones Utiles


Existen multiples configuraciones utiles que les podemos ingresar a nuestros spiders para ellos se le pasan las configuraciones desde el atributo _custom_settings_:
- FEED_URI = Nombre del archivo y extension como se guardara la informacion extraida
- FEED_FORMAT = Tipo de extension en la que se guardara la informacion
- CONCURRENT_REQUESTS = Numero de peticiones que puede ejecutar simultaneamente
- MEMUSAGE_LIMIT_MB = Cantidad maxima de memoria ram que puede utilizar en megabytes
- MEMUSAGE_NOTIFY_MAIL = Lista de correos a los que se les notifica cuando se exceda el limite de ram
- ROBOTSTXT_OBEY = Boleano que permite daber si seguiran los lineamientos de ROBOTSTXT o no (Si haremos caso o no a las paginas que nos dicen podemos entrar)
- USER_AGENT = String que nos permite configurar el agente desde el que estamos haciendo la peticion
- FEED_EXPORT_ENCODING = tipo de enconding para la salida
