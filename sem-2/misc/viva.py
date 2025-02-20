import re

def match(string):
    if not re.search(r"[.,:;!?]$", string): 
        return False

    middle_index = len(string) // 2

    if len(string) % 2 == 0:  
        if len(string) >= 2 and re.search(r"[pqr]", string[middle_index - 1] + string[middle_index]):
            return True
    else:  
        if len(string) >= 1 and re.search(r"[pqr]", string[middle_index]):
            return True

    return False

strings = [
    "abdjrjhf!.", 
    "abcpd.", 
    "abcp.", 
    "abcp", 
    "abc", 
    "abpd", 
    "abp",
    "ab", 
    "a", 
    "ap." 
]

for string in strings:
    if match(string):
        print(f"'{string}' matches")
    else:
        print(f"'{string}' does not match")