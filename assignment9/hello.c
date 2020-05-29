#include <stdio.h>
#include <pthread.h>
#include <unistd.h> 

void *hello(void *arg)
{
    while (1)
    {
        printf("Hello\n");
        sleep(1);
    }
}

int main(void)
{
    pthread_t hello_thread;
    
    pthread_create(&(hello_thread), NULL, hello, NULL);
    pthread_join(hello_thread, NULL);
    printf("Outside of thread");   
    return 0;
}