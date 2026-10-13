#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int x, int y, int n) {
    if(x == y) return 0;
    
    vector<int> visited(y + 1, 0);
    queue<int> q;
    
    q.push(x);
    
    while (!q.empty()) {
        int current = q.front();
        q.pop();
        
        long long next_vals[3] = {
            (long long) current + n,
            (long long) current * 2,
            (long long) current * 3
        };
        
        for(long long next: next_vals) {
            if(next > y || visited[next] > 0) continue;
            
            visited[next] = visited[current] + 1;
            
            if(next == y) {
                return visited[next];
            }
            
            q.push(next);
        }
    }
    return -1;
}