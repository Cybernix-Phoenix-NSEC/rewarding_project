// 2 3 1 34  45
// To find the first occurrence of the int at the given position;

#include <iostream>
using namespace std;

int occurrence(int A[], int size, int t){
    static int mSize = size;
    if(size == 0){
        return -1;
    }

    if(A[0]==t){
        return mSize - size;
    }

    int smallValue = occurrence(A+1, size -1, t);

    if(smallValue){
        return smallValue;
    }

    

};

int main()
{
    int n, t;
    cin >> n >> t;
    int *P = new int[n];
    for (int i = 0; i < n; i++)
    {
        cin >> P[i];
    }

    int x = occurrence(P, n, t);
    cout << x << endl;
    return 0;
}