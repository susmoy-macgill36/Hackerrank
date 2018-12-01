
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    long long int array1[100000];
    long long int total=0;
    cin>>n;

    for ( int i=0;i<n;i++)
    {
        cin>>array1[i];
    }
     for ( int i=0;i<n;i++)
    {
        total+=array1[i];
    }
  cout<<total;
  return 0;

}

