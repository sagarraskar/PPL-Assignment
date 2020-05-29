#include <stdio.h> 
#include <pthread.h> 
#include <unistd.h> 
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int hr, min, sec;
pthread_t second_thread, minute_thread, hour_thread;
bool stop = false;

void* thread1(void* arg) 
{ 
	while(!stop){
		while (sec < 60) {
			sleep(1);
			system("clear");
			printf("########################################        Digital Clock          #########################################\n\n\n");
			printf("\n\n\n\t\t\t\t\t\t%02d:%02d:%02d\n", hr, min, sec);
			sec++;
		}
		sec = 0;
	}
}

void* thread2(void* arg)
{	
	int j = 0;
	while(!stop){
		while (min < 60) {
			
			if (j == 0){
				sleep(60-sec+1);
				j++;
			}
			else
				sleep(60);
			min++;
		}
		min = 0;
	}
}	


void* thread3(void* arg)
{	
	int j = 0;
	while(!stop){
		while (hr < 24) {
			if (j == 0){
				sleep((60-min+1) * 60);
				j++;
			}
			else
				sleep(60);
			hr++;
		}
		hr = 0;
	}
}
    
int main() {
 	char c;
	time_t rawtime;
	struct tm * timeinfo;
	time(&rawtime);
	timeinfo = localtime(&rawtime);
	hr = timeinfo->tm_hour;
	min = timeinfo->tm_min; 
	sec = timeinfo->tm_sec;
    
	pthread_create(&second_thread,NULL,thread1,NULL); 
	pthread_create(&minute_thread,NULL,thread2,NULL); 
	pthread_create(&hour_thread,NULL,thread3,NULL);

	pthread_join(second_thread,NULL);
	pthread_join(minute_thread,NULL);
	pthread_join(hour_thread,NULL);

    return 0; 
} 
