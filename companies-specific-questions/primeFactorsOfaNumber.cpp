#include<bits/stdc++.h>

using namespace std;

int main(){

    int n;
    cin>>n;

   for(int i=2 ;n>1 ;i++ )
    {
        while(n%i==0){
            printf( "%d ",i);
            n/=i;
        }
    }
    

    return 0;
}