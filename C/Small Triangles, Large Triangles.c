#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;
float getArea(triangle t) {
	float s = (t.a+t.b+t.c) / 2.0;
	return sqrt(s*(s-t.a)*(s-t.b)*(s-t.c));
}

void sort_by_area(triangle* tr, int n) {
	for (int i=1; i<n; i++) {
		int j = i;
		triangle temp = tr[i];
		while (j>0 && getArea(temp)<getArea(tr[j-1])) {
			tr[j] = tr[j-1];
			j--;
		}
		tr[j] = temp;
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}