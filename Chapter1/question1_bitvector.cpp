#include <string>
#include <iostream>
#include <bitset>

using namespace std;

bool isUniqueChars(string str);

int main(void) {
  string case1 = "pythonista";
  isUniqueChars(case1);
}

bool isUniqueChars(string str) {
  cout << "\nisUniqueChars(" << str <<") is called" <<endl;
  int checker = 0;
  for (int i = 0; i < str.size(); i++) {
    cout << "iter = " << i << " | str(" << i << ") = " << str[i] << endl;
    int val = str[i] - 'a';
    cout << "val(b):\t\t" << bitset<32>(val) << endl;
    cout << "1 << val(b):\t" << bitset<32>(1 << val) << endl;
    if ((checker & (1 << val)) > 0) {
      return false;
    }
    checker |= (1 << val);
    cout << "checker(b)\t" << bitset<32>(checker) << endl;
  }
  return true;
}
