import { expect } from "chai";
import "mocha";
import { argumentsLength } from "./solution";

describe("Return length of arguments passed", () => {
  it("should pass test case #1", () => {
    const result: number = argumentsLength({}, null, "3");
    expect(result).to.equals(3);
  });

  it("should pass test case #2", () => {
    const result: number = argumentsLength(1,2);
    expect(result).to.equals(2);
  });

  it("should pass test case with zero arguments given", () => {
    const result: number = argumentsLength();
    expect(result).to.equals(0);
  });

  it("should pass test case with 1 argument given", () => {
    const result: number = argumentsLength([]);
    expect(result).to.equals(1);
  });

});