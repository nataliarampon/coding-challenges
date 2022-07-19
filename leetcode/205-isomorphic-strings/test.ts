import { expect } from "chai";
import "mocha";
import { solution, solutionMoreMemoryButFaster } from "./solution";

describe("Isomorphic strings", () => {
    describe("One hashmap, slower", () => {
        it("should pass test case #1", () => {
            const originalString = "egg";
            const comparisonString = "add";
            const expectedResult = true;
    
            const result:boolean = solution(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #2", () => {
            const originalString = "foo";
            const comparisonString = "bar";
            const expectedResult = false;
    
            const result:boolean = solution(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #3", () => {
            const originalString = "paper";
            const comparisonString = "title";
            const expectedResult = true;
    
            const result:boolean = solution(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #4", () => {
            const originalString = "bbbaaaba";
            const comparisonString = "aaabbbba";
            const expectedResult = false;
    
            const result:boolean = solution(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #5", () => {
            const originalString = "badc";
            const comparisonString = "baba";
            const expectedResult = false;
    
            const result:boolean = solution(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass no change test case", () => {
            const originalString = "dummy";
            const comparisonString = "dummy";
            const expectedResult = true;
    
            const result:boolean = solution(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    });

    describe("Two hashmaps, faster", () => {
        it("should pass test case #1", () => {
            const originalString = "egg";
            const comparisonString = "add";
            const expectedResult = true;
    
            const result:boolean = solutionMoreMemoryButFaster(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #2", () => {
            const originalString = "foo";
            const comparisonString = "bar";
            const expectedResult = false;
    
            const result:boolean = solutionMoreMemoryButFaster(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #3", () => {
            const originalString = "paper";
            const comparisonString = "title";
            const expectedResult = true;
    
            const result:boolean = solutionMoreMemoryButFaster(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #4", () => {
            const originalString = "bbbaaaba";
            const comparisonString = "aaabbbba";
            const expectedResult = false;
    
            const result:boolean = solutionMoreMemoryButFaster(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #5", () => {
            const originalString = "badc";
            const comparisonString = "baba";
            const expectedResult = false;
    
            const result:boolean = solutionMoreMemoryButFaster(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass no change test case", () => {
            const originalString = "dummy";
            const comparisonString = "dummy";
            const expectedResult = true;
    
            const result:boolean = solutionMoreMemoryButFaster(originalString, comparisonString);
            expect(result).to.equal(expectedResult);
        });
    });
    
});