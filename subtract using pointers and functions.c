#include <stdio.h>

int sub(int *a,int *b);
int main()
{
   int a,b,res;
   printf("Enter two numbers\n");
   scanf("%d %d\n",&a,&b);
   res = sub(&a,&b);
   printf("%d",res);
   return 0;
}

int sub(int *a, int *b)
{
    return *a-*b;   
}