#include <cstdint>
#include <iostream>
#include <cmath>

bool isPrime(std::int_least32_t& n){
	if(n%2==0){
		if(n==2){
			return(true);
		} else {
		return(false);
		}
	} else {
		for (std::int_least32_t i = 3; i < static_cast<std::int_least32_t>(std::pow(n,0.5))+1; i+= 2) {
			if(n%i==0){
				return(false);
			}
		}
	}
	return(true);
}

int main(){
	std::int_least64_t total = 0;
	for (std::int_least32_t i = 2; i < 2000000; ++i){
		if (isPrime(i)){
			total += i;
		}
	}
	std::cout << total << std::endl;
	return(0);
}
