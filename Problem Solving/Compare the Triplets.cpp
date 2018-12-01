#include<bits/stdc++.h>
using namespace std;

int main ()
{
    int Alice=0,Bob=0;
    int a[3],b[3];
    for (int i=0;i<3;i++)
    {
        cin>>a[i];

    }
     for (int i=0;i<3;i++)
    {
        cin>>b[i];

    }


    for (int i = 0 ; i <3; i++)
    {
        if(a[i]>b[i])
            Alice++;
        if(a[i]<b[i])
            Bob++;

    }

    cout<<Alice<<" "<<Bob;


}
