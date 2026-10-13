#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(int k, vector<int> tangerine) {    
    map<int, int> counts;
    
    for(int t : tangerine) {
        counts[t]++;
    }
    
    vector<int> freq;
    for (auto it : counts) {
        freq.push_back(it.second);
    }
    
    sort(freq.begin(), freq.end(), greater<int>());
    
    int answer = 0;
    int total = 0;
    
    for (int count: freq) {
        total += count;
        answer++;
        
        if(total >= k) {
            break;
        }
    }
    return answer;
}