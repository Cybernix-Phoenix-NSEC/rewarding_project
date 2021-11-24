#include<bits/stdc++.h>

using namespace std;


int sumOfDigits(int n){
int sum=0;
if(n==0)
return 0;

sum= n%10+sumOfDigits(n/10);
return sum;

}


int main(){
    
    int n;
    cin>>n;

cout<<sumOfDigits(n);

    return 0;
}