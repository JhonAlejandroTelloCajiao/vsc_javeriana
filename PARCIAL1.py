
def compareDNASeq(dnaString1, dnaString2):
    if len(dnaString1) != len(dnaString2):
        print("The sequences are different")
        return 0
    else:
        for index in range(len(dnaString1)):
            if dnaString1[index] != dnaString2[index]:
                print("The sequences are the same")
                return 1 
        print("The sequences are different")
        return 0
compareDNASeq("CTAGCGAT", "CATGTATAG")






