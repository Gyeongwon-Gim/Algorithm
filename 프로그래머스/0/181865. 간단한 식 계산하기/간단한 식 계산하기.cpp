#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string binomial) {
    stringstream ss(binomial);
    string word;
    vector<string> result;
    
    while (ss >> word){
        result.push_back(word);
    }
    
    int a = stoi(result[0]);
    string op = result[1];
    int b = stoi(result[2]);
    
    if (op == "+"){
        return a + b;
    } else if (op == "-"){
        return a - b;
    } else if (op == "*"){
        return a * b;
    }
}