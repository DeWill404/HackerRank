#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MIN_ELEMENT 1
#define MAX_ELEMENT 1000000
int  sum (int count,...) {
	int SUM;

	va_list list;
	va_start(list, count);

	SUM = va_arg(list, int);
	for (int i=1; i<count; i++) { SUM += va_arg(list, int); }

	va_end(list);

	return SUM;
}

int min(int count,...) {
	int MIN, element;

	va_list list;
	va_start(list, count);

	element = MIN = va_arg(list, int);
	for (int i=1; i<count; i++)
		if ( (element=va_arg(list,int)) < MIN )
			MIN = element;
	
	return MIN;
}

int max(int count,...) {
	int MAX, element;

	va_list list;
	va_start(list, count);

	element = MAX = va_arg(list, int);
	for (int i = 1; i < count; i++)
		if ((element = va_arg(list, int)) > MAX)
			MAX = element;

	return MAX;
}

int test_implementations_by_sending_three_elements() {