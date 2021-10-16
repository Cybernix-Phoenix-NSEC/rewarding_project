#include<bits/stdc++.h>
#include<math.h>
using namespace std;



int main(){

    int n;
    cin>>n;
int temp = n;
int rev= 0;


    while(temp){
        int last_digit = temp%10;
        rev= rev*10+last_digit;
        temp/=10;

    }
    if (rev == n)
    cout<<"Palindrome number";
    else
    cout<<" NOT Palindrome number";
}
