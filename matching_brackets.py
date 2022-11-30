#Dictionaries, Lists, Conditionals


def is_paired(input_string):
    test = []
    mydict["("] = ")"
    mydict["["] = "]"
    mydict["{"] = "}"
    for ch in input_string:
        if (ch in "([{"):
            test.append(ch)
        if (ch in ")]}"):
            if len(test) >= 1:
                last = test.pop()
                if (mydict[last] != ch):
                    return False
            else:
                return False
            
    if len(test) == 0:
        return True
    else:
        return False
            
            
            
        
        
