#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_map<string, int> cloth_map;
    // 각 종류별 의상 개수 세기
    for(auto c: clothes){
        cloth_map[c[1]]++;
    }
    
    // 조합의 수 계산하기
    int answer = 1;
    for(auto it: cloth_map){
        answer *= (it.second + 1);
    }
    
    return answer - 1;
}