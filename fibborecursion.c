#include<stdio.h>
int fibonacci(int n);
int main(){
    int n;
    scanf("%d",&n);
    printf("The %dth element of fibonacci series is %d",n,fibonacci(n));
    return 0;
}
int fibonacci(int n){
    if(n==0 || n==1){
        return 0;
    }
    if(n==2){
        return 1;
    }
    else{
        return fibonacci(n-1)+fibonacci(n-2);
    }
}