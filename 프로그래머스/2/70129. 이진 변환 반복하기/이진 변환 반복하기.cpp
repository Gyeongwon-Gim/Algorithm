#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    int transform_count = 0;
    int removed_zero_count = 0;
    
    vector<int> answer;
    while ( s != "1") {
        // 0 제거
        // 1의 개수가 곧 0을 제거한 x의 길이
        int zeros = 0;
        int ones = 0;
        
        for(char c : s) {
            if (c == '0') {
                zeros++;
            } else {
                ones++;
            }
        }
        
        removed_zero_count += zeros;
        transform_count++;
        // 2진법 표현 변환
        s = "";
        int temp = ones;
        while (temp > 0) {
            s = to_string(temp % 2) + s;
            temp /= 2;
        }
    }
    return {transform_count, removed_zero_count};
}