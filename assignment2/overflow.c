#include <stdio.h>

int main(void)
{
    int arr[5] = {1, 2, 3, 4, 5};
    arr[6] = 10;
    printf("%d\n", arr[6]);
    return 0;
}