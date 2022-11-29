#Dictionaries, Lists, Conditionals


def is_paired(input_string):
    test = []
    for ch in input_string:
        if (ch == "(") or (ch == "[") or (ch == "{"):
            test.append(ch)
        elif (ch == ")"):
            if test[-1] == "(":
                del test[-1]
            else:
                return False
        elif (ch == "]"):
            if test[-1] == "[":
                del test[-1]
            else:
                return False
        elif (ch == "}"):
            if test[-1] == "{":
                del test[-1]
            else:
                return False
    if len(test) == 0:
        return True
    else:
        return False
            
            
            
        
        
