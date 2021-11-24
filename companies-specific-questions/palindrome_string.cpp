#include<bits/stdc++.h>

using namespace std;

 int main(){
    cout<<"hi.."<<endl;
    string str;
    cin>>str;

    int n= str.size();
    int s= 0;
    int e= n-1;

    for(int i=0 ; i<n/2 ; i++){
        if (str[s]!=str[e]){
                cout<<"Not palindrome string ";
                return 0;
        }
       
    else 
    continue;

    }

    cout<<"Palindrome string"<<endl;
}