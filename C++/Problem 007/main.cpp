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

vector<uint_fast64_t> primes;

void genPrimes(long n){
    if (primes.size() <= 1){
        primes.push_back(2);
        primes.push_back(3);
    }
    for(uint_fast64_t i = primes.back()+2;
    primes.size() <= static_cast<size_t>(n);
    i+= 2){
        for (uint_fast64_t& prime : primes){
            if (prime == primes.back()) {
                primes.push_back(i);
                break;
            }
            else if (i%prime == 0){
                break;
            }
        }
    }
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        genPrimes(static_cast<long>(n));
        cout << primes[n-1] << endl;
        /*for(auto prime: primes){
            cout << prime << ",";
        }
        cout << endl;*/
    }
    return 0;
}
