import { expect } from "chai";
import "mocha";
import { solution } from "./solution";

describe("Find pivot index", () => {
    it("should pass test case #1", () => {
        const input:Array<number> = [1,7,3,6,5,6];
        const expectedResult = 3;

        const result:number = solution(input);
        expect(result).to.equal(expectedResult);
    });

    it("should pass test case #2", () => {
        const input:Array<number> = [1,2,3];
        const expectedResult = -1;

        const result:number = solution(input);
        expect(result).to.equal(expectedResult);
    });

    it("should pass test case #3", () => {
        const input:Array<number> = [2,1,-1];
        const expectedResult = 0;

        const result:number = solution(input);
        expect(result).to.equal(expectedResult);
    });
});