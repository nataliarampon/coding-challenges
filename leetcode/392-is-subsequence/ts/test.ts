import { expect } from "chai";
import "mocha";
import { solution } from "./solution";

describe("Is subsequence", () => {
    it("should pass test case #1", () => {
        const subsequence = "abc";
        const originalString = "ahbgdc";
        const expectedResult = true;

        const result:boolean = solution(subsequence, originalString);
        expect(result).to.equal(expectedResult);
    });

    it("should pass test case #2", () => {
        const subsequence = "axc";
        const originalString = "ahbgdc";
        const expectedResult = false;

        const result:boolean = solution(subsequence, originalString);
        expect(result).to.equal(expectedResult);
    });

    it("should pass test case #3", () => {
        const subsequence = "ac";
        const originalString = "ahbgdcccccc";
        const expectedResult = true;

        const result:boolean = solution(subsequence, originalString);
        expect(result).to.equal(expectedResult);
    });

    it("should pass same string test case", () => {
        const subsequence = "abc";
        const originalString = "abc";
        const expectedResult = true;

        const result:boolean = solution(subsequence, originalString);
        expect(result).to.equal(expectedResult);
    });

    it("should pass trivial test case", () => {
        const subsequence = "";
        const originalString = "";
        const expectedResult = true;

        const result:boolean = solution(subsequence, originalString);
        expect(result).to.equal(expectedResult);
    });

    it("should pass low-length test case", () => {
        const subsequence = "a";
        const originalString = "b";
        const expectedResult = false;

        const result:boolean = solution(subsequence, originalString);
        expect(result).to.equal(expectedResult);
    });
});