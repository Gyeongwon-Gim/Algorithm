function solution(ineq, eq, n, m) {
    let answer = 0;
    if (ineq == '>' && eq == '='){
        if (n >= m){
            return 1
        }
        return 0
    } else if (ineq == '<' && eq == '=') {
        if (n <= m){
            return 1
        }
        return 0
    } else if (ineq == '>' && eq == '!') {
        if (n > m){
            return 1
        }
        return 0
    } else if (ineq == '<' && eq == '!') {
        if (n < m){
            return 1
        }
        return 0
    }
    
}