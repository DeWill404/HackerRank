#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return -(strcmp(a, b));
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int d1=1, d2=1;
    for (int i=1; i<strlen(a); i++) {
        int isDistinct = 1;
        for (int j=0; j<i; j++) {
            if (a[i]==a[j]) {
                isDistinct = 0;
                break;
            }
        }
        if (isDistinct) { d1++; }
    }
    for (int i=1; i<strlen(b); i++) {
        int isDistinct = 1;
        for (int j=0; j<i; j++) {
            if (b[i]==b[j]) {
                isDistinct = 0;
                break;
            }
        }
        if (isDistinct) { d2++; }
    }
    return d1-d2 ? d1-d2 : lexicographic_sort(a,b);
}

int sort_by_length(const char* a, const char* b) {
    return strlen(a)-strlen(b) ? strlen(a)-strlen(b) : lexicographic_sort(a,b);
}

void swap(char *a, char *b) {
    char *temp = (char*)malloc(strlen(a)*sizeof(char));
    strcpy(temp, a);
    
    a = (char *)realloc(a, strlen(b)*sizeof(char));
    b = (char *)realloc(b, strlen(a)*sizeof(char));

    strcpy(a, b);
    strcpy(b, temp);

    free(temp);
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    for (int i=1; i<len; i++) {
        int j = i;
        char *temp = (char *)malloc(strlen(*(arr+i))*sizeof(char));
        strcpy(temp, *(arr+i));
        while(j>0 && cmp_func(temp, *(arr+j-1))<0) {
            *(arr+j) = (char *)realloc(*(arr+j), strlen(*(arr+j-1))*sizeof(char));
            strcpy(*(arr+j), *(arr+j-1));
            j--;
        }
        *(arr+j) = (char *)realloc(*(arr+j), strlen(temp)*sizeof(char));
        strcpy(*(arr+j), temp);
        free(temp);
    }
}


int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}