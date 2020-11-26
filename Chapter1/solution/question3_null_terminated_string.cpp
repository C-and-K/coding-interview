#include <stdio.h>
#include <cstring>

int main(void){
  char* str1 = "Hello, Konabe";
  char* str2 = "Hello, \0Konabe";

  // 終端文字列ががある場合
  printf("%s\n", str1);
  printf("%s\n", str2);

  // 終端文字列がなければ
  str1[strlen(str1) - 1] = '!';
  printf("%s\n", str1);

  return 0;
}