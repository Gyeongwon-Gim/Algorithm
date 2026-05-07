function solution(num_str) {
    let answer = 0;
    const num_list = num_str.split('');
    for (let i=0; i<num_list.length; i++){
        answer += Number(num_list[i]);
    }
    return answer;
}