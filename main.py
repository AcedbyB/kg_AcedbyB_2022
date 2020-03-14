import sys

def check(s1, s2):
    if len(s1) != len(s2):
        return False
    encode =  [-1 for i in range(1000)]
    cur = 0
    for i in range(0,len(s1)):
        original_char = ord(s1[i]) 
        tranformed_char = ord(s2[i])
        if encode[original_char] == -1:
            encode[original_char] = tranformed_char
        else:
            if encode[original_char] != tranformed_char:
                return False
    return True

def main():
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    if check(s1,s2) == True:
        print("true")
    else:
        print("false")
    
main()