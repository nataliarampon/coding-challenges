
export function solution(input:Array<number>): Array<number> {
    input.reduce((accumulator,_,index,array) => array[index] += accumulator);
    return input;
}