#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int abs(int x) { return x<0 ? -(x) : x; }
int max(int a, int b) { return a>b ? a : b; }

int main() 
{

	int n;
	scanf("%d", &n);

	int c = n-1;

	for (int i=0; i<2*n-1; i++) {
		for (int j=0; j<2*n-1; j++) {
			printf("%d ", max(abs(i-c),abs(j-c))+1);
		}
		printf("\n");
	}

	return 0;
}