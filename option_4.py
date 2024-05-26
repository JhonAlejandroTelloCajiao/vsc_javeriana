def compareSequence(genetic_list, pattern, percent):
    if opcSec == 4:
        while True:
            pattern = input("Enter a valid sequence of DNA or RNA: ")
            percent = float(input("Enter a valid percentage (0.0 - 0.1)")) 
            for element in pattern:
                if element in ["A","T","C","G","U"]:
                    break
                else:
                    print("Invalid Sequence")       
            if not 0.0 <= percent <= 1.0: 
                print("Invalid Percentage")
            else:
                break
    found = False
    for i in range(len(genetic_list)):
        genS = genetic_list[i]
        if len(genS) != len(pattern): 
            continue
        coincidence = 0
        for j in range(len(genS)):
            if genS[j] == pattern[j]:
                coincidence += 1
        similarity = coincidence/len(pattern)
        if similarity >= percent:
            print("Secuencia parecida encontrada en:", [i])
            found = True
    if not found: 
        print("No se encuentran resultados")
compareSequence(["ATCGTAAGC"])