#include <bits/stdc++.h>

using namespace std;

int main()
{
  long long int test,total;
  cin>> test;
  total=test;
 for(int index=0;index<test;index++)
 {
    long long int task;
    cin>>task;
    int C[1441]={0},J[1441]={0},start,end,temp,joker=0;
    set<pair<pair<int,int>,int>> time;
    string ans="";

    for(int t=0;t<task;t++)
    {
        ans+="*";
        cin>>start>>end;
        time.insert(make_pair(make_pair(start,end),t));
    }
    int maxc=0,maxj=0,minc=0,minj=0,c=0,j=0;
       for (auto const &x : time) { 
        start=x.first.first;
        end=x.first.second;
        if(start>=maxc)c=0;
        if(start>=maxj)j=0;
        if(c==0)
        {
            c=1;
            minc=start;
            maxc=end;
            ans[x.second]='C';
        }
        else if(j==0)
        {
            j=1;
            minj=start;
            maxj=end;
            ans[x.second]='J';
        }
        else
        {
            joker=1;
        }
        
        
    } 
  
    cout<<"Case #"<<index+1<<": ";
    if(joker==1)
    {
        cout<<"IMPOSSIBLE";
    }
    else
        cout<<ans;
    if(index+1!=test)
     cout<<endl;
    

 }
}