function solution(a, b) {
    const a_b = String(a) + String(b);
    const b_a = String(b) + String(a);
    
    if(a_b >= b_a){
        return Number(a_b)
    }
    return Number(b_a);
}