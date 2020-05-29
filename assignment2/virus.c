#include <stdio.h>
#include <string.h>

void virus()
{
    printf("Virus is in control");
}

void function1(char* str)
{
    char arr[5];
    strcpy(arr, str);
}
int main(int argc, char *argv[]){
    function1(argv[1]);

    printf("Exeucted Normally");
    return 0;
}