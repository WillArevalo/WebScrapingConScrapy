# Multiple Callbacks

Para resolver el problema de tener información duplicada como es el title podemos hacer uso de los multiples callbacks al crear varios metodos parse

En este caso lo que se hace es invocar el nuevo metodo desde el callback pasando las listas de los elementos que se van extrayendo desde los argumentos del callback con el argumento _cb_kwargs_