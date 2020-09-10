#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	char string[100];
	do {

		fgets(string, 100, stdin);
		printf("%s", string);

	}  while(string[strlen(string)-1] == '\n');
	return 0;
}
