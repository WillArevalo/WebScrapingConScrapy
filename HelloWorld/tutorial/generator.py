# Generador(iterador) return parcial con yield

def challenge():
    for i in range(2, 99, 2):
        yield i


my_iter = challenge()

while True:
    print(next(my_iter))