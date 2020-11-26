## 宿題：終端文字について、issueにまとめる C++ #include<cstdio>にprintfが入ってる
# - char型の配列を使って文字列を作り、char型の先頭ポインタを使って%sで表示させる
# char str[128]; printf("%s", str); --> ちゃんと表示できればOK (文字列リテラルは使用禁止)
# - 終端文字列を外すとどうなるか
def solve(string, num):
    string = string[:num+1]
    result_str = ""
    for ch in string:
        if ch == " ":
            result_str += "%20"
        else:
            result_str += ch
    return result_str

def main():
    assert(solve("this is a book   ", 14) == "this%20is%20a%20book")
    assert(solve("  ", 1) == "%20")
    assert(solve("this  is  a  book ", 17) == "this%20%20is%20%20a%20%20book")

if __name__ == "__main__":
    main()