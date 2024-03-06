
#Define the function and pass it two string-type parameters representing DNA sequences 
def compareDNASeq(dnaString1, dnaString2):
    if len(dnaString1) != len(dnaString2): #Comparing the length of characters between the two DNA sequences 
        print("The sequences are different")
        return 0
    else:
        for index in range(len(dnaString1)):
            if dnaString1[index] != dnaString2[index]: #Checking each base of the sequences 
                print("The sequences are different")
                return 0 
        print("The sequences are the same")
        return 1
compareDNASeq("CTAGCGAT", "CTAGCGAG")

#Se define la función y se le entrega como parámetro un string que será una cadena de ADN 
def showPositions(dnaString):
    ask_for_base = input("Ingrese Base Nitrogenada: ") #Se le solicita los datos al usuario 
    if ask_for_base != "A" and ask_for_base != "T" and ask_for_base != "C" and ask_for_base != "G": #Verificación del input
        print("Base inválida")
    for i in range(len(dnaString)): # Se crea un rango con la posición de los caracteres del parámetro de la función 
        if dnaString[i] == ask_for_base: #Para cada iteración, se busca la coincidencia
            print("Base encontrada en la posición", i) #Se imprimen las posiciones donde hubo coincidencias 
showPositions("CCATATTAGGG") #Se llama la función con el argumento 





