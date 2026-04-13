#include<iostream>
using namespace std;
class car
{
   string brand,model;
   int year,rate;
   public:
      car()
      {
	 brand=" ";
	 model=" ";
	 year=rate=0;
      }
      ~car()
      {
	 cout<<"Destruction Executed.";
      }
      void getdata()
      {
	 cout<<"Enter the car brand..";
	 cin>>brand;
	 cout<<"Enter the car model..";
	 cin>>model;
	 cout<<"Enter the year..";
         cin>>year;
	 cout<<"Enter the price of the car..";
	 cin>>rate;
      }
};
int main()
{
   car b;
   b.getdata();
   return 0;
}   
