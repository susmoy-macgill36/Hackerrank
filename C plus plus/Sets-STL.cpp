#include<bits/stdc++.h>
using namespace std;
int main ()
{


    set<long long int> s;
    int n;
    long long int a,b;
    cin>>n;
    for (int i = 0 ; i<n;i++)
    {
        cin>>a>>b;
        if(a==1)
        {

            s.insert(b);
        }
        else  if(a==2)
        {
            s.erase(b);


        }
        else if(a==3)
        {
            if (s.find(b)== s.end()){
                cout<<"No"<<endl;
            }
            else
                cout<<"Yes"<<endl;

        }

    }


}



