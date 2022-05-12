import random #sirve para trabajar numeros aleatorios


def run():
    numero_aleatorio = random.randint(1, 100) #en este caso se saca un numero aleatorio entero del 1-100
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande ")
        else:
            print("Buscar un numero mas pequeño")
        numero_elegido = int(input("Elige otro numero "))
    print("¡Ganaste!")            
    

if __name__ == '__main__':
    run()
