export function solution(input: string, comparison: string): boolean {
    const substitutions:Record<string, string> = {};

    for(let i = 0; i < input.length; i++) {
        if(input[i] in substitutions) {
            if (substitutions[input[i]] !== comparison[i]) {
                return false;
            }
        } else {
            if (Object.values(substitutions).includes(comparison[i])) {
                return false;
            }
            substitutions[input[i]] = comparison[i];
        }
    }
    return input.length == comparison.length;
}

export function solutionMoreMemoryButFaster(input: string, comparison: string): boolean {
    const substitutionsInput:Record<string, string> = {};
    const substitutionsComparison:Record<string, string> = {};

    for (let i = 0; i < input.length; i++) {
        if (input[i] in substitutionsInput || comparison[i] in substitutionsComparison) {
            if (substitutionsInput[input[i]] != comparison[i] || substitutionsComparison[comparison[i]] != input[i]) {
                return false;
            }
        }
        substitutionsInput[input[i]] = comparison[i];
        substitutionsComparison[comparison[i]] = input[i];
    }
    return input.length == comparison.length;
}
