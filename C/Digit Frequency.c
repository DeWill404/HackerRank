#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

	char s[1000];
	int n[10]={0};

	fgets(s, 1000, stdin);

	for (int i=0; i<strlen(s); i++) {
		if ( s[i]>='0' && s[i]<='9' ) {
			n[s[i]-'0']++;
		}
	}

	for (int i=0; i<10; i++) { printf("%d ", n[i]); }

	return 0;
}
