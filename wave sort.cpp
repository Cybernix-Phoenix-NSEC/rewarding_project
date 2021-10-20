#include<iostream>
using namespace std;
void Swap(int arr[],int i,int j){
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
void wavesort(int arr[],int n){
    for(int i=1;i<n;i+=2){
        if(arr[i] > arr[i-1]){
            Swap(arr,i,i-1);
        }
        if(arr[i] > arr[i+1] && i <= n-2){
            Swap(arr,i,i+1);
        }
    }
}
int main(){
    int n;
    cout<<"Enter the size of array - ";
    cin>>n;
    int arr[n];
    cout<<"Enter the elements of array - ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    wavesort(arr,n);
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
