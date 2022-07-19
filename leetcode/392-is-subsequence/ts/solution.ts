export function solution(subsequence: string, originalString: string): boolean {
    let i = 0;
    let j = 0;

    if (subsequence.length > originalString.length) {
        return false;
    }
    
    while (i < subsequence.length && j < originalString.length) {
        if (subsequence[i] === originalString[j]) {
            i++;
        }
        j++;
    }

    return i == subsequence.length;
}