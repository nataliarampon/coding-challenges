import { expect } from "chai";
import "mocha";
import { maxDepth } from "./solution";

describe("Find maximum nesting depth of the parentheses", () => {
  it("should pass test case #1", () => {
    const result: number = maxDepth("(1+(2*3)+((8)/4))+1");
    expect(result).to.equals(3);
  });

  it("should pass test case #2", () => {
    const result: number = maxDepth("(1)+((2))+(((3)))");
    expect(result).to.equals(3);
  });

  it("should return 0 for empty string", () => {
    const result: number = maxDepth("");
    expect(result).to.equals(0);
  });

  it("should return 0 if string has no parentheses", () => {
    const result: number = maxDepth("1");
    expect(result).to.equals(0);
  });
});