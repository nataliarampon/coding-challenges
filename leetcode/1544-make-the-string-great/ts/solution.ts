export function makeGood(s: string): string {
  const stack: Array<string> = [];
  const TOP_OF_STACK = -1;

  for (const char of s) {
    const prevChar = stack.at(TOP_OF_STACK);
    if (isReverseCase(char, prevChar)) {
      stack.pop();
    } else {
      stack.push(char);
    }
  }
  return stack.join('');
}

function isReverseCase(currentChar: string, prevChar?: string) {
  const ASCII_DISTANCE_BETWEEN_CASES = 32;
  return Math.abs(currentChar.charCodeAt(0) - (prevChar?.charCodeAt(0) || 0)) === ASCII_DISTANCE_BETWEEN_CASES;
}