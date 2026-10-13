#include <string>
#include <vector>
#include <iostream>

using namespace std;

int countOnes(int num) {
    int count = 0;
    while (num > 0) {
        if (num % 2 == 1) {
            count ++;
        }
        num /= 2;
    }
    return count;
}

int solution(int n) {
    int targetOnes = countOnes(n);
    int nextNum = n + 1;
    
    while (true) {
        if(countOnes(nextNum) == targetOnes) {
            return nextNum;
        }
        nextNum++;
    }
    
}