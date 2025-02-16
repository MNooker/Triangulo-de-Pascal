def triangulopascal(f, e):
    fila_trian = []                                             #almacenar las filas del triángulo en una lista.
    for i in range(f):
        coef = 1                                                #el coeficiente siempre es 1.
        fila_valores = []
        for j in range(i + 1):
            fila_valores.append(str(coef ** e))                 #se eleva el coeficiente al exponente que se ingrese.
            coef = coef * (i - j) // (j + 1)                    #se calcula la relacion recursiva

        fila_trian.append(" ".join(fila_valores))               #se empieza a generar la cadena.
    ancho_max = len(fila_trian[-1])                             #se determina el ancho maximo para calcular

    for fila in fila_trian:                                     #Imprimimos cada fila centrada según el ancho máximo.
        print(fila.center(ancho_max))

if __name__ == "__main__":
    f = int(input("Ingrese el número de filas: "))
    expo = int(input("Ingrese el exponente: "))
    triangulopascal(f, expo)