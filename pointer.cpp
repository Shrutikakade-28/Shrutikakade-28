#include <iostream>
using namespace std;
class Simple{
    public:
    int a=10;
};
//this pointer code
class Sample{
    int a,b;
    public:
    void input(int a, int b){
        this-> a= b;
        this-> b= a;
    }
    void output(){
        cout<<"a= "<<a<<endl<<"b= "<<b<<endl;
    }
};

//pointers and arrays


int main(){
    Simple obj;
    Simple *ptr; //decleration of class pointer
    ptr = &obj; //initilazation of class pointer
    cout<<"Object of class-"<<obj.a<<endl;
    cout<<"Pointer of clas-"<<ptr->a<<endl;

    Sample x;
    x.input(5,8);
    x.output();
    return 0;
}