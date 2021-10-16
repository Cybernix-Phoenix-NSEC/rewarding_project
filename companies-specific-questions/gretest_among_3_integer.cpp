#include<bits/stdc++.h>

using namespace std;

int main(){
    int a,b,c;

    cin>>a>>b>>c;

    int max= (a>b and a>c)?(a):(b>c ?(b):(c));

cout<<endl;
cout<<"greatest of threee numbers is "<<max;


    return 0;

}