#include <string>
#include <vector>

using namespace std;

string solution(int age) {
    string answer = "";
    string s = to_string(age);
    
    for (char c : s) {
        answer += 'a' + (c - '0');
    }
    return answer;
}
    