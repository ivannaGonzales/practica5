#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define SIZE 1000000
#define NUM_THREADS 4

void *bubble_sort(void *arg);

int main() {
 pthread_t threads[NUM_THREADS];
 int *array = malloc(SIZE * sizeof(int));
 for (int i = 0; i < SIZE; i++) {
   array[i] = rand() % SIZE;
 }

 clock_t start_time = clock();

 for (int i = 0; i < NUM_THREADS; i++) {
   pthread_create(&threads[i], NULL, bubble_sort, &array[i * SIZE / NUM_THREADS]);
 }

 for (int i = 0; i < NUM_THREADS; i++) {
   pthread_join(threads[i], NULL);
 }

 clock_t end_time = clock();
 double time_spent = (double)(end_time - start_time) / CLOCKS_PER_SEC;

 printf("Tiempo de ejecución: %f segundos\n", time_spent);

 free(array);
 return 0;
}

void *bubble_sort(void *arg) {
 int *array = (int *)arg;
 int start = 0;
 int end = SIZE / NUM_THREADS;

 for (int i = start; i < end - 1; i++) {
   for (int j = start; j < end - i - 1; j++) {
       if (array[j] > array[j + 1]) {
           int temp = array[j];
           array[j] = array[j + 1];
           array[j + 1] = temp;
       }
   }
 }

 return NULL;
}
