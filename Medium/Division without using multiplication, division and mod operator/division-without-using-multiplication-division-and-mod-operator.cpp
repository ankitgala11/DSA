//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;



// } Driver Code Ends
//User function Template for C++


class Solution
{
    public:
    long long divide(long long dividend, long long divisor) 
    {
        if(dividend == INT_MIN and divisor == -1)
            return INT_MAX;
            
        int sign = dividend>0 ^ divisor>0 ? -1 : 1;
        long long dvd = llabs(dividend), dvs = llabs(divisor);
        long long ans=0;
        
        while(dvd >= dvs){
            long temp = dvs, m = 1;
            while(temp<<1 <= dvd){
                temp <<= 1;
                m <<= 1;
            }
            dvd -= temp;
            ans += m;
        }
        return sign*ans;
    }
};

//{ Driver Code Starts.
int main() {
	int t;
	cin >> t;

	while (t--)
	{

		long long a, b;
		cin >> a >> b;
		
		Solution ob;
		cout << ob.divide(a, b) << "\n";
	}

	return 0;
}

// } Driver Code Ends