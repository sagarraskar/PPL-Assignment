#include <stdio.h>


int fact(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }

    return n * fact(n-1);
}

int main(void)
{
    int n = 3;
    int res = fact(n);
    printf("%d\n", res);
    return 0;
}