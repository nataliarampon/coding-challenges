export function maxDepth(s: string): number {
  const stack: Array<string> = [];
  let maxDepthCount = 0;

  for (const char of s) {
    if (char === '(') {
      stack.push(char);
    } else if (char === ')') {
      if (stack.length > maxDepthCount) {
        maxDepthCount = stack.length;
      }
      stack.pop();
    }
  }
  
  return maxDepthCount;
}
