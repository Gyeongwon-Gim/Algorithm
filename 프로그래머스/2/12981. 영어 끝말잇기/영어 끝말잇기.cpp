#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    unordered_set<string> used_words;
    
    used_words.insert(words[0]);
    
    for(int i = 1; i < words.size(); i++){
        string prev = words[i - 1];
        string curr = words[i];
        
        if(prev.back() != curr.front() || used_words.count(curr) > 0) {
            int person = (i % n) + 1;
            int turn = (i / n) + 1;
            return {person, turn};
        }
         
         used_words.insert(curr);
    }
    
    return {0, 0};
}