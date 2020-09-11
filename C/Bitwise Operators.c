#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {

	int a=0, b=0, c=0;

	for (int i=1; i<n; i++) {
		for (int j=2; j<=n; j++) {
			if (i < j) {
				if ( (i&j)<k ) {
					if ( (i&j) > a ) {
						a = i&j;
					}
				}
				if ( (i|j) < k ) {
					if ( (i|j) > b ) {
						b = i|j;
					}
				}
				if ( (i^j) < k ) {
					if ( (i^j) > c ) {
						c = i^j;
					}
				}
			}
		}
	}

	printf("%d\n", a);
	printf("%d\n", b);
	printf("%d\n", c);

}

int main() {
	int n, k;
  
	scanf("%d %d", &n, &k);
	calculate_the_maximum(n, k);
 
	return 0;
}
