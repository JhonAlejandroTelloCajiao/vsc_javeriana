
if opcSec == 3:
        while True:
            pattern = input("Enter a valid sequence of DNA or RNA: ") 
            for element in pattern:
                if element in ["A","T","C","G","U"]:
                    break
                else:
                    print("Invalid Sequence")