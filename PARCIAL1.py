
#Se define la función y se le entrega como parámetro una cadena de texto en mayúsculas
def isDNAString(string): 
    count_1 = 0        # Se define un contador que será el que contenga la cantidad de caracteres ajenos a una secuencia de ADN 
    for chr in string: # Se recorre la cadena de texto elemento por elemento 
        if chr != "A" and chr != "T" and chr != "C" and chr != "G":
            count_1 += 1
    if count_1 > 0:
        print("No es una secuencia de ADN")
        print("Caracteres extraños:", count_1)
    else:
        print("Es una secuencia de ADN")
isDNAString("CASA") #Se llama la función con el argumento entregado 

def showPositions(dnaString):
    ask_for_base = input("Ingrese Base Nitrogenada: ")
    for i in range(len(dnaString)):
        if i == ask_for_base:
            print("Base encontrada en la posición", dnaString[i])
        else: 
            print("Base inválida")
showPositions("AACATA")






