def invertOrComplement(genetic_list):
    if genetic_list == []:
        print("Lista Vacía")
        return genetic_list
    last_sequence = genetic_list[-1]
    new_sequence = ""

    if "U" in last_sequence:  # ARN sequence
        new_sequence = last_sequence[::-1]
        print("Creación de Cadena Inversa Completa: " + new_sequence)
    else:  # ADN sequence
        for base in last_sequence:
            if base == "A":
                new_sequence += "T"
            elif base == "T":
                new_sequence += "A"
            elif base == "C":
                new_sequence += "G"
            elif base == "G":
                new_sequence += "C"
        print("Creación de Cadena Complementaria Completa: " + new_sequence)
    genetic_list.append(new_sequence)
    return genetic_list
invertOrComplement(["AGTCGTTAG", "AUCGAAUCAUUGAC"])