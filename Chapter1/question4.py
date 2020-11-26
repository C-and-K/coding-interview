# 文字数が奇数だった場合は、１個の文字が奇数個で、それ以外偶数個
# 偶数だった場合は、全部の文字が偶数個ある

def solve(string):
    # 小文字と大文字を区別しないように、変換が必要です
    tmp_dict = {}
    for ch in string:
        if ch in tmp_dict:
            tmp_dict[ch] += 1
        else:
            tmp_dict[ch] = 1
    
    if len(string) % 2 == 0:
        return all([v % 2 == 0 for v in tmp_dict.values()])
    else:
        return 1 == sum([v % 2 for v in tmp_dict.values()])


def main():
    assert(solve("aabbccd") == True)
    assert(solve("aabbcc") == True)
    assert(solve("abcd") == False)

if __name__ == "__main__":
    main()

'''
00101 mask 00100
00101 & 00011
= 00001
'''

