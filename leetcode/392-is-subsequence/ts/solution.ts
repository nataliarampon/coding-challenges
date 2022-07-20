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

export function dynamicProgrammingSolution(subsequence: string, originalString: string): boolean {
    // handle empty strings (it's either this or using conditionals)
    subsequence = "X" + subsequence;
    originalString = "X" + originalString;

    const matrix:boolean[][] = new Array(subsequence.length).fill(false).map(() => new Array(originalString.length).fill(false));
    const subLength:number = subsequence.length;
    const oriLength:number = originalString.length;

    if (subLength > oriLength) {
        return false;
    }
    
    for (let i = 0; i < subLength; i++) {
        for (let j = i; j < oriLength; j++) {
            if (subsequence[i] == originalString[j]) {
                if (i == 0 || j == 0) {
                    matrix[i][j] = true;
                } else {
                    // if a new character matches, it will be a match if the previous character on the subsequence matched up to one character before on the string
                    matrix[i][j] = matrix[i-1][j-1];
                }
            } else {
                if (j == 0) {
                    matrix[i][j] = false;
                } else {
                    // if no match happens, the new subsequence will still match if it previously matched to the character before on the string
                    // if it did not match anything new, it matters not if the subsequence (i) matched before or not, because we are not furthering our knowledge
                    matrix[i][j] = matrix[i][j-1];
                }
            }
        }
    }

    return matrix[subLength-1][oriLength-1];
}