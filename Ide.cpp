#include <iostream>
using namespace std;

string name="";
string password="";
void main() {
    string n;
    string p;
    cin>>n;
    cin>>p;
	name="\""+n+"\"";
	password="\""+p+"\"";
	cout<<"Username : "<<name<<endl;
	cout<<"Password :"<<password<<endl;
}
