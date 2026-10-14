#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int solution(vector<int> topping) {
    int answer = 0;
    
    unordered_map<int, int> brother;
    unordered_set<int> elder;

    
    for (int t: topping) {
        brother[t]++;
    }
    
    int brother_kinds = brother.size();
    
    for(int t: topping) {
        elder.insert(t);
        
        brother[t]--;
        if(brother[t] == 0) {
            brother_kinds--;
        }
        
        if(elder.size() == brother_kinds) {
            answer++;
        }
    }
    return answer;
}