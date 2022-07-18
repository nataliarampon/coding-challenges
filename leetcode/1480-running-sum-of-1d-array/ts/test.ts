import { expect } from "chai";
import "mocha";
import { solution } from "./solution";

describe("Running sum of 1D array", () => {
    it("should pass test case #1", () => {
        const input:Array<number> = [1,2,3,4];
        const expectedResult:Array<number> = [1,3,6,10];

        const result:Array<number> = solution(input);
        expect(result).to.deep.equal(expectedResult);
    });

    it("should pass test case #2", () => {
        const input:Array<number> = [1,1,1,1,1];
        const expectedResult:Array<number> = [1,2,3,4,5];

        const result:Array<number> = solution(input);
        expect(result).to.deep.equal(expectedResult);
    });

    it("should pass test case #3", () => {
        const input:Array<number> = [3,1,2,10,1];
        const expectedResult:Array<number> = [3,4,6,16,17];

        const result:Array<number> = solution(input);
        expect(result).to.deep.equal(expectedResult);
    });

    it("should pass empty test case", () => {
        const input:Array<number> = [];
        const expectedResult:Array<number> = [];

        const result:Array<number> = solution(input);
        expect(result).to.deep.equal(expectedResult);
    });

    it("should pass zeroed array test case", () => {
        const input:Array<number> = [0,0,0];
        const expectedResult:Array<number> = [0,0,0];

        const result:Array<number> = solution(input);
        expect(result).to.deep.equal(expectedResult);
    });

    it("should pass negative array test case", () => {
        const input:Array<number> = [-1,-3,-4];
        const expectedResult:Array<number> = [-1,-4,-8];

        const result:Array<number> = solution(input);
        expect(result).to.deep.equal(expectedResult);
    });

    it("should pass negative and positive array test case", () => {
        const input:Array<number> = [-1,2,-4];
        const expectedResult:Array<number> = [-1,1,-3];

        const result:Array<number> = solution(input);
        expect(result).to.deep.equal(expectedResult);
    });

    it("should return the array itself when it's an one-element array", () => {
        const input:Array<number> = [-10];
        const expectedResult:Array<number> = [-10];

        const result:Array<number> = solution(input);
        expect(result).to.deep.equal(expectedResult);
    });
});