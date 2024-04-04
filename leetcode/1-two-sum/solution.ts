export function twoSum(nums: number[], target: number): number[] {
    const NOT_FOUND_RETURN_VALUE: number[] = [-1, -1];

    const numberToIndexMap: Record<number, number> = {};

    for (let i = 0; i < nums.length; i ++) {
      if (numberToIndexMap[target - nums[i]] != undefined) {
        return [numberToIndexMap[target - nums[i]], i];
      } else {
        numberToIndexMap[nums[i]] = i;
      }
    }

    return NOT_FOUND_RETURN_VALUE;
}
