export function solution(input: Array<number>):number {
    const rightSum = [...input];

    input.reduce((acc,_,i,arr) => arr[i] += acc);
    rightSum.reduceRight((acc,_,i,arr) => arr[i] += acc);

    for(let i = 0; i < input.length; i++) {
        if(input[i] == rightSum[i]) {
            return i;
        }
    }
    return -1;
}