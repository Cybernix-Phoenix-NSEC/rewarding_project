#include <iostream>
 
using namespace std;
const int MAX = 3;
 
int main () {
   int  var[MAX] = {10, 100, 200};
 
 int* ptr = var;
   for (int i = 0; i < MAX; i++) {
      *var = 466;    // This is a correct syntax but you cannot increment the value of var by: var ++
      //as var is a constant that points to the address of the first element of the array!
      cout<<var[i] <<" ";
      ptr++;
   }
   return 0;
}