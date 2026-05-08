// #include <string>
#include <vector>
// #include <iostream> 
#include <stack>
using namespace std;

vector<int> solution(vector<int> prices) {
    int n = prices.size();
    vector<int> answer(n);
    stack<int> s;
    
    for(int i = 0; i < n; i++){
        while (!s.empty() && prices[s.top()] > prices[i]) {
            int idx = s.top();
            s.pop();
            answer[idx] = i - idx; // 떨어진 시점 - 들어온 시점 = 버틴시간
        }
        s.push(i);
    }
    
    // 끝까지 가격이 떨어지지 않은 나머지 시점들 처리
    while (!s.empty()){
        int idx = s.top();
        s.pop();
        answer[idx] = n - 1 - idx;
    }
    
    return answer;
}