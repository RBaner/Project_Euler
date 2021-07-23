#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

long multiplyDigits(int n);

long problem(int n,int k,string num){
    long max{0};
    for (int i = 0; i< n-k ;++i){ //set starting location
        long temp = multiplyDigits(stoi(num.substr(i,k)));
        //cout << "i = " << i << ", k = "<< k <<", temp = " << temp<< ", max = " << max << ", substr = "<< num.substr(i,k) << endl;
        if(max < temp){
            max = temp;
        }
    }
    return(max);
}

long multiplyDigits(int n){
    long product = 1;
 
    while (n != 0)
    {
        product = product * (n % 10);
        n = n / 10;
    }
 
    return(product);
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        int k;
        cin >> n >> k;
        string num;
        cin >> num;
        cout << problem(n,k,num) << endl;
    }
    return 0;
}
