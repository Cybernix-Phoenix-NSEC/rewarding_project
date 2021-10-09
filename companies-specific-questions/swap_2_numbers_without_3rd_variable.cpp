#include<bits/stdc++.h>

using namespace std;

// int  main(){

//     int a,b;
//     cin>>a>>b;

//     a=a+b;
//     b=a-b;
//     a=a-b;

//     cout<<a<<" "<< b<<endl;

//     return 0;

// }

int main(){
    int a,b;
    cin>>a>>b;


    a=a^b;
    b=a^b;
    a=a^b;

   cout<<a<<" "<< b<<endl;
}