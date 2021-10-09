#include<bits/stdc++.h>
#include<math.h>
using namespace std;

bool armstrong(int n){
  //    digit = (int) log10(num) + 1;
  int len = to_string(n).length();
  int sum=0 ;
int org= n;
cout<<len<<endl;
      while (n)
    {
        int r = n%10;
        sum += pow(r, len);
        n = n/10;
    }

return (sum==org);
}

int main(){
    int n,power;
    cin>>n;
    int digit = (int) log10(n) + 1;
    int temp= n;
int sum=0 ;
    while(temp){

        int r= temp%10;
        //int power= pow(r,digit); wromg
      // int  power = round(pow(r, digit));
       sum =sum+round(pow(r,digit));
        //cout<<sum ;
        //sum += r*r*r;
        temp/=10;
    }

    if (n==sum )
    cout<<"Armstrong Number";
    else
    cout<<"Not ArmStrong Number";

return 0;
}