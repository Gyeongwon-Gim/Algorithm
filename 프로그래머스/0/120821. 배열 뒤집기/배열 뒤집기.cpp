#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> result;
    for (int i=(num_list.size()-1); i >= 0; i--) {
        result.push_back(num_list[i]);
    }
    return result;
}