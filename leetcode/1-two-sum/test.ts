import { expect } from "chai";
import "mocha";
import { twoSum } from "./solution";

describe("Find indexes of two sum in an array", () => {
  it("should pass test case #1", () => {
    const result: number[] = twoSum([2,7,11,15], 9);
    expect(result).to.deep.equals([0,1]);
  });

  it("should pass test case #2", () => {
    const result: number[] = twoSum([3,2,4], 6);
    expect(result).to.deep.equals([1,2]);
  });

  it("should pass test case #3", () => {
    const result: number[] = twoSum([3,3], 6);
    expect(result).to.deep.equals([0,1]);
  });

  it("should return no-solution vector if no solution can be found", () => {
    const result: number[] = twoSum([3,2], 6);
    expect(result).to.deep.equals([-1,-1]);
  });

  it("should return no-solution vector if array is empty", () => {
    const result: number[] = twoSum([], 6);
    expect(result).to.deep.equals([-1,-1]);
  });
});