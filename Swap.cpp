//Swapping
#include <iostream>
using namespace std;
void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}
void swap(float &a, float &b){
    float temp = a;
    a = b;
    b = temp;
}
void swap(char &a, char &b){
    char temp = a;
    a = b;
    b = temp;
}
int main(){
    int x,y;
    cout<<"Enter values of x and y: "<<endl;
    cin>>x>>y;
    swap(x,y);
    cout<<"Before swapping x= "<<x<<",y= "<<y<<endl;
    cout<<"After swapping x= "<<y<<",y= "<<x<<endl;
    return 0;
}
