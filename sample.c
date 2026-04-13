#include<stdio.h>
#define N=5
int s[N];
int top=-1;
void push()
{
   int x;
   printf("Enter the  element ..");
   scanf("%d",&x);
   if(top > N-1)
      printf("Stack Overflow..");
   else
   {
      top=top+1;
      s[top]=x;
   }
} 
void display()
{
   int i;
   for(i=top;i>=0;i--)
      printf("Element %d..",s[1]);
