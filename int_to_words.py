
#First create indices to match scales and number units
ones = [
    "",
    "one ",
    "two ",
    "three ",
    "four ",
    "five ",
    "six ",
    "seven ",
    "eight ",
    "nine ",
    "ten ",
    "eleven ",
    "twelve ",
    "thirteen ",
    "fourteen ",
    "fifteen ",
    "sixteen ",
    "seventeen ",
    "eighteen ",
    "nineteen ",
]

twenties = [
    "",
    "",
    "twenty ",
    "thirty ",
    "forty ",
    "fifty ",
    "sixty ",
    "seventy ",
    "eighty ",
    "ninety ",
]

scales = [
    "",
    "thousand ",
    "million ",
    "billion ",
    "trillion ",
    "quadrillion ",
    "quintillion ",
]

def num999(n): 
    #Stores singles digit
    c = n % 10  

    #Stores tens digit  
    b = int(((n % 100) - c) / 10)   

    #Stores hundreds digit ()
    a = int(((n % 1000) - (b * 10) - c) / 100)  
    t = ""
    h = ""

    if a != 0 and b == 0 and c == 0:
        t = ones[a] + "hundred "
    elif a != 0:
        t = ones[a] + "hundred and "
    if b <= 1:
        h = ones[n % 100]
    elif b > 1:
        h = twenties[b] + ones[c]
    st = t + h
    return st

def number_to_words(num):
    if num == 0:
        return "zero"

    i = 3
    n = str(num)
    word = ""
    k = 0

    while i == 3:
        # slice te last three digits
        nw = n[-i:] 

        #keeps everything else
        n = n[:-i]  

        if int(nw) == 0:
            word = num999(int(nw)) + scales[int(nw)]+ word #recursively call num999 function %& concat with scales and word previous value
        else:
            word = num999(int(nw)) + scales[k] + word
        if n == "":
            i = i + 1  #To stop iterating the loop once string becomes empty
        k += 1
    

    #Return output with last character(space removed)
    return word[:-1] 
