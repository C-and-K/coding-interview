def solve(input):
    unique_dict = {}
    
    for c in input:
        if c in unique_dict:
            return False
        else:
            unique_dict[c] = 1

    return True

# 新たなデータ構造が使えない場合
def solve2(input):
    # time: O(n^2)
    # space: O(n)
    for i, ch in enumerate(input):
        for ch2 in input[i+1:]:
            if ch == ch2:
                return False
    return True

def main():
    assert(solve("avawjdioajwodjao") == False)
    assert(solve("abcdefghijk") == True)
    assert((solve("a") == True))

    assert(solve2("avawjdioajwodjao") == False)
    assert(solve2("abcdefghijk") == True)
    assert(solve2("a") == True)
    
if __name__ == "__main__":
    main()  
