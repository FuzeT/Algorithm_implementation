#include <iostream>
using std::cout;
using std::endl;

void print(int a[], int n, int p){
    cout<<p<<" : ";
    for(int i=0; i<n; i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

void InsertSort(int a[], int n){
    for(int i=1; i<n; i++){
        if(a[i]<a[i-1]){
            int x = a[i];
            int j = i-1;
            a[i] = a[i-1];
            while(a[j]>x){
                a[j+1] = a[j];
                j--;
            }
            a[j+1] = x;
        }
        print(a, n, i);
    }
}

int main(){
    int a[] = {5,4,3,2,1};
    print(a, 5, 0);
    InsertSort(a, 5);
}
