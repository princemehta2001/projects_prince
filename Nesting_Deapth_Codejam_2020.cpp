#include <bits/stdc++.h>

using namespace std;

int main()
{
  long long int test,total;
  cin>> test;
  total=test;
  while( test--)
 {
    
     long long int max=0,temp,diff;
     string s="",ans=""; 
     cin>>s;
   for(long long int i=0;i<s.size();i++)
	{
		temp=s[i]-48;
		if(temp>max)
		{
		  diff=temp-max;
		  max=temp;
	          while(diff--)ans+="(";	  
		}
		else if(temp<max)
		{
		  diff=max-temp;
		  while(diff--)ans+=")";
		  max=temp;
		}
		ans+=temp+48;
        
      

    }
    while(max--)ans+=")";
    cout<<"case #"<<total-test<<": "<<ans<<endl;


}
}