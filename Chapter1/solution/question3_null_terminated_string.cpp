#include <stdio.h>

int main(void){
    char* str = "Hello, Konabe\0";
    char* str2 = "Hello, \0Konabe";

    printf("%s\n", str);
    printf("%s\n", str2);

    return 0;
}