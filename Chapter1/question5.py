import string

def solve(str1, str2):
    for i in range(len(str1)):
        for l in string.ascii_lowercase:
            inserted = insert(str1, i, l)
            replaced = replace(str1, i, l)
            if inserted == str2 or replaced == str2:
                return True
        deleted = delete(str1, i)
        if deleted == str2:
            return True
    
    return False

def insert(input_str:str, index: int, insert_str: str):
    return input_str[:index] + insert_str + input_str[index:]

def delete(input_str: str, index: int):
    return input_str[:index] + input_str[index + 1:]

def replace(input_str:str, index:int, replace_string: str):
    return input_str[:index] + replace_string + input_str[index+1:]

def main():
    assert(solve("pale", "ple") == True)
    assert(solve("pales", "pale") == True)
    assert(solve("pale", "bale") == True)
    assert(solve("pale", "bake") == False)

if __name__ == "__main__":
    main()