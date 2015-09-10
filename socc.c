#include <stdio.h>
#include <stdlib.h>

typedef struct
{
	char author[50];
	int citedby;
	int year;
	char key[50];
} SOCC;

SOCC s[2000] =
{
	{"Sangho Shin", 11, 2005},
	{"Sung-Sop Lee", 9, 2005},
	{"Zhengtao Yu", 7, 2005},
	{"Addo-Quaye", 77, 2005},
	{"Jun-Cheng Chi", 7, 2005},
	{"Chih-Peng", 8, 2005, "CMOS"},
	{"Chih-Peng", 3, 2005, "Hybrid"},
	{NULL, 0, 0, NULL}
};

int cmp(const void *a, const void *b) 
{ 
	return (*(SOCC *)b).citedby > (*(SOCC *)a).citedby; 
} 

int main(int argc, char *argv[])
{
	int i;
	
	qsort(s, 100, sizeof(s[0]), cmp);

	for (i = 0; i < 5; i++)
	{
		printf("%s %d %d %s\n", s[i].author, s[i].citedby, s[i].year, s[i].key);
	}
	
	return 0;
}
