#include <string>
#include <vector>

using namespace std;

string solution(string rsp) {
    string answer = "";
    for (char c : rsp) {
        if (c == '2') {
            answer += '0';
            continue;
        }
        if (c == '5') {
            answer += '2';
            continue;
        }
        answer += '5';
    }
    return answer;
}