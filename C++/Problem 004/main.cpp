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
#include <cstdint>

using namespace std;

bool isPalindrome (uint_fast32_t n){
    if(
        (n/1)%10 == (n/100000)%10 &&                 //digit 1 == digit 6
        (n/10)%10 == (n/10000)%10 &&                 //digit 2 == digit 5
        (n/100)%10 == (n/1000)%10                    //digit 3 == digit 4
    ) return(true);
    else return(false);
}

uint_fast32_t problem(uint_fast32_t max){
    uint_fast32_t n = max -1;
    while (n >= 101101){
        if(isPalindrome(n)){
            for(uint_fast16_t i = 100; i < 1000; ++i ){
                if((n%i == 0) && ((n/i) < 1000)){
                    return(n);
                }
            }
        }
        --n;
    }
    return(0);
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        cout << problem(n) << endl;
        //cout << (isPalindrome(n) ? "Is a plaindrome!" : "Is not a palindrome") << endl;
    }
    return 0;
}
