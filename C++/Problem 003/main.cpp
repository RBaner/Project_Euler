#include <algorithm>
#include <cmath>
#include <vector>
#include <iostream>
#include <cstdint>

using namespace std;

vector<uint_fast64_t> primes(static_cast<size_t>(pow(10,6)));

void genPrimes(long n){
    if (primes[0] == 0){
        primes[0] = 2;
        primes[1] = 3;
        primes[2] = 5;
    }
    for(uint_fast64_t sweep{*(find(primes.begin(),primes.end(),0)-1)+2};
    sweep < ceilf64(pow(n,0.5f)+1);
    sweep+=2){
        for (uint_fast64_t& prime : primes){
            if (prime == 0) {
                prime = sweep;
                break;
            }
            else if (sweep%prime == 0){
                break;
            }
        }
    }
}

int_fast64_t problem(long& n){
    genPrimes(n);
    while(n%2 == 0){n /= 2;}
    uint_fast32_t largestFactor{3};
    while(n != 1){
        while(n%largestFactor == 0){
            n /= largestFactor;
        }
        largestFactor += 2;
    }
    return(largestFactor-2);
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        long n;
        cin >> n;
        cout << problem(n) << endl;
        //genPrimes(n);
    }
    return 0;
}
