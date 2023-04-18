#include <iostream>
#include <math.h>
using namespace std;

class test{
    public:
        string te;
        int waw;
        test(string x,int y);
        int lol();
};

test::test(string x,int y){
    waw = y;
    te = x;
};

int test::lol(){
    return waw ++;
};


int main(){
    test x("ok",4);
    for (int i; i<6;i++){
        x.lol();
    };
    int tes = (x.waw == 10) ? 3 : 7; 
    cout << tes;
    return 0;
}
