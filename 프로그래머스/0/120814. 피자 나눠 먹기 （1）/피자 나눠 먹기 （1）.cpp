#include <string>
#include <vector>

using namespace std;

int solution(int n) {    
    int 몫 = n / 7;
    int 나머지 = n % 7;
    
    if (나머지 > 0) {
        return 몫 + 1;
    } 
    return 몫;
}