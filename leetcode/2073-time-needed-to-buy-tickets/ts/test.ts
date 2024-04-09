import { expect } from "chai";
import "mocha";
import { timeRequiredToBuy } from "./solution";

describe("Find time needed to buy tickets for k-th person on queue", () => {
  it("should pass test case #1", () => {
    const result: number = timeRequiredToBuy([2,3,2], 2);
    expect(result).to.equals(6);
  });

  it("should pass test case #2", () => {
    const result: number = timeRequiredToBuy([5,1,1,1], 0);
    expect(result).to.equals(8);
  });

  it("should pass test case #3", () => {
    const result: number = timeRequiredToBuy([1, 1, 2], 0);
    expect(result).to.equals(1);
  });

});