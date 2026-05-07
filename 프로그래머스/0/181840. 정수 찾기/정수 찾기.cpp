#include <vector>
using namespace std;
    
int solution(vector<int> num_list, int n) {
    for(int x: num_list) {
        if (x == n ) return 1;
    }
    return 0;
}
