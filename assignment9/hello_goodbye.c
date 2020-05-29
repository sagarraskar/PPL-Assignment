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
void *goodbye(void *arg)
{
    while (1)
    {
        printf("Goodbye\n");
        sleep(1);
    }
}
int main(void)
{
    pthread_t hello_thread, goodbye_thread;
    
    pthread_create(&(hello_thread), NULL, hello, NULL);
    pthread_create(&goodbye_thread, NULL, goodbye, NULL);
    pthread_join(hello_thread, NULL);
    pthread_join(goodbye_thread, NULL);
  
    return 0;
}