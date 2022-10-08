# Removing all types but true characters (no white space, punctuation, commas, periods, etc)

def extract_char(string):
    rvm_list = [" ","\t","\n",".",",","!",":",";"]
    l0 = []
    for char in string:
        if char not in rvm_list:
            l0.append(char)
    return "".join(l0)

print(extract_char("The!dog,swam    in the lake"))






