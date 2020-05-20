// C implementation of digital clock 
#include <stdio.h> 
#include<stdlib.h>
#include<unistd.h>
#include <time.h> 
#include<pthread.h>

//declaring globally to use in both threads ssame value
time_t s;                         // time_t is : This is a variable type suitable for storing the calendar time.
struct tm* current_time;          // struct tm : This is a (variable type) structure used to hold the time and date

pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER; 


  
void *functionName1(void *vargp){

pthread_mutex_lock(&lock); 
printf("Inside thread 1 -time is found in seconds\n");
s = time(NULL);       // time function returns the time in seconds   
pthread_mutex_unlock(&lock); 
}

void *functionName2(void *vargp){

printf("Inside thread2 - Time in seconds is calculated in hrs, min and sec \n\n");
pthread_mutex_lock(&lock); 
current_time = localtime(&s);   		// the localtime function converts a calendar time (pointed to by timer) and returns a pointer to a  												structure. // to get current time 
printf("Current Time is - %02d:%02d:%02d\n\n", current_time->tm_hour, current_time->tm_min, current_time->tm_sec);
							 			 // print time in minutes, hours and seconds

pthread_mutex_unlock(&lock);
}


int main(){

	pthread_t thread_id1, thread_id2;
	printf("Inside Main before thread\n\n");
	
	pthread_create(&(thread_id1), NULL, functionName1, NULL);
	pthread_create(&(thread_id2), NULL, functionName2, NULL);
	
	pthread_join(thread_id1, NULL);
	pthread_join(thread_id2, NULL);
	
	printf("Inside Main after thread\n\n");
	return 0;
}

  
