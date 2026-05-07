function solution(num_list) {
    var count = 0;
    for(let i=0; i<num_list.length; i++){
        num = num_list[i];
        while (num > 1){
            if(num%2 == 0){
                num /= 2;
                count += 1;
            }else{
                num -= 1;
            num /= 2;
            count += 1;
            }
        }     
    }
    return count;
}