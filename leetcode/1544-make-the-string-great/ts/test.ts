import { expect } from "chai";
import "mocha";
import { makeGood } from "./solution";

describe("Make the string great", () => {
  it("should pass test case #1", () => {
    const result: string = makeGood("leEeetcode");
    expect(result).to.equals("leetcode");
  });

  it("should pass test case #2", () => {
    const result: string = makeGood("abBAcC");
    expect(result).to.equals("");
  });

  it("should return an empty string for empty string", () => {
    const result: string = makeGood("");
    expect(result).to.equals("");
  });

  it("should return string if string has no adjacent reverse case letters", () => {
    const result: string = makeGood("a");
    expect(result).to.equals("a");
  });
});