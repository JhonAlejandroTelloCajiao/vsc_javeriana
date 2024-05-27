
while True: 
    if opcSec not in ["Y", "y", "N", "n"]:
        print("Invalid Input")
    if selectSec not in [1,2]:
       print("Invalid Input")
    for element in chain:
        if element in ["A","T","C","G","U"]:
            break
        else:
            print("Invalid Sequence")  
