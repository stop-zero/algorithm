function solution(n) { 
    return n % 7 === 0 ? ~~(n/7) : ~~(n/7)+1;
}
