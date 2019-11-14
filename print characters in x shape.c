#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
int i,j,l;
char a[100];
scanf("%s",&a);
l=strlen(a);
for(i=0;i<l;i++)
{
    for(j=0;j<l;j++)
    {
        if(i==j)
        {
            printf("%c",a[i]);
        }
        else if(i+j==l-1 && i!=j)
        {
            printf("%c",a[j]);
        }
        else
        {
            printf(" ");
        }
    }
    printf("\n");
}
return 0;
}