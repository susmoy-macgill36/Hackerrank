/*
https://www.hackerrank.com/challenges/arrays-ds/problem
/**/


#include <bits/stdc++.h>
using namespace std;
int main()
{
     int n;
 int arr[n],arr2[n];
 vector <int> v;

 cin>>n;
 for (int i  =0; i <n ;i++)
 {

     cin>> arr[i];
v.push_back(arr[i]);
 }

reverse(v.begin(), v.end());

for(int i = 0 ; i < n ; i++)
{
    arr2[i] = v[i];

}
for (int i  =0; i <n ;i++)
 {

   printf("%d ",arr2[i]);


 }
}
