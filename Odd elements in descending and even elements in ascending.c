#include<conio.h>
#include<string.h>
void main()
{
int a[100];
int i,j,s,temp;
printf("Enter the size of array:");
scanf("%d",&s);
for(i=0;i<s;i++)
{
    scanf("%d",&a[i]);
}
for(i=0;i<s;i+=2)
{
    for(j=i+2;j<s;j+=2)
    {
        if(a[i]<a[j])
        {
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
    }
}
for(i=1;i<s;i+=2)
{
    for(j=i+2;j<s;j+=2)
    {
        if(a[i]>a[j])
        {
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
    }
}
for(i=0;i<s;i++)
{
    printf(" \t%d",a[i]);
}
return 0;
}