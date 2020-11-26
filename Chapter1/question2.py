def solve(string1, string2):
    s1_dict = {}
    s2_dict = {}

    if len(string1) != len(string2):
        return False

    for s in string1:
        if s not in s1_dict:
            s1_dict[s] = 1
        else:
            s1_dict[s] += 1

    for s in string2:
        if s not in s2_dict:
            s2_dict[s] = 1
        else:
            s2_dict[s] += 1

    if len(s1_dict) != len(s2_dict):
        return False

    for k, v in s1_dict.items():
        if v != s2_dict[k]:
            return False

    return True


def main():
    assert(solve("abc", "abc") == True) # True
    assert(solve("abc", "bac") == True) # False
    assert(solve("aac", "bac") == False) # False
    assert(solve("aacssss", "bac") == False) # False
    assert(solve("aabcde", "bcadea") == True) # True
    

if __name__ == "__main__":
    main()  
