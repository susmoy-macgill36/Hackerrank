#include<bits/stdc++.h>
using namespace std;

int main ()
{
    vector<int> v;
    int n,z,i;
    cin>>n;
    for ( i = 0 ; i < n; i++)
    {
        cin>>z;
        v.push_back(z);

    }
    sort(v.begin(),v.end());
     for ( i = 0 ; i < n; i++)
    {
        printf("%d ",v[i]);

    }
}
