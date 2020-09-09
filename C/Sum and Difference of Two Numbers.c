#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int Ia, Ib;
	float Fa, Fb;

	scanf("%d %d", &Ia, &Ib);
	scanf("%f %f", &Fa, &Fb);
	
	printf("%d %d\n", Ia+Ib, Ia-Ib);
	printf("%.1f %.1f\n", Fa+Fb, Fa-Fb);

	return 0;
}
