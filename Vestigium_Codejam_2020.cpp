#include <bits/stdc++.h>

using namespace std;

int main()
{
  long long int test,total;
  cin>> test;
  total=test;
  while( test--)
 {
     long long int size;
      cin >> size;
      
       map <long long int ,  map<long long int ,long long int>> row;
       map <long long int , map<long long int ,long long int>> col;
       
       map<long long int , int > rows_counted;
       map<long long int , int > cols_counted;
      long long int count_row=0 ;
       long long int count_col = 0;
       long long int sum =0;
       
      
      for(long  long int i=0 ; i < size ; i++)
{
   for (long  long int j=0 ; j<size ;j++ )
    {
        long long int temp ;
         cin >> temp;
         
         if(i==j) sum+=temp;

        row[ i ] [ temp ] += 1;
        
        if( row [i] [ temp ] == 2 && rows_counted[i]==0 )
            {
                 rows_counted[i]++;
                 count_row++;
            }

         col[ j ] [ temp ] += 1;
        
        if( col [j] [ temp ] == 2 && cols_counted[j]==0 )
             {
                 cols_counted[j]++;
                 count_col++;
             }


    }



}
 cout<<"Case #"<<(total-test)<<": ";
 cout<<sum<<" "; 
 cout<<count_row<<" ";
 cout<<count_col<<endl;



 }


}