def is_paired(input_string):
    br_open = 0
    sq_open = 0
    fl_open = 0
    last = 0
    for ch in input_string:
        if (br_open > 0):
            if (ch == "]") or (ch == "}"):
                return False
            elif (ch == ")"):
                br_open = br_open -1
                continue
        if (sq_open > 0):
            if (ch == ")") or (ch == "}"):
                return False
            elif (ch == "]"):
                sq_open = sq_open -1
                continue
        if (fl_open > 0):
            if (ch == ")") or (ch == "]"):
                return False
            elif (ch == "}"):
                fl_open = fl_open -1
                continue
        if (ch == "("):
            br_open = br_open +1
            last = 1
        elif (ch == "["):
            sq_open = sq_open +1
            last = 2
        elif (ch == "{"):
            fl_open = fl_open +1
            last = 3
        elif ((ch == ")") or (ch == "]") or (ch == "}")):
            return False
    if (br_open == 0) and (sq_open == 0) and (fl_open == 0):
        return True
    else:
        return False
        
