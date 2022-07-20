import { expect } from "chai";
import "mocha";
import { dynamicProgrammingSolution, solution } from "./solution";

describe("Is subsequence", () => {
    describe("2 pointers approach", () => {
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
    
        it("should pass test case #4", () => {
            const subsequence = "ace";
            const originalString = "abcde";
            const expectedResult = true;
    
            const result:boolean = solution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #5", () => {
            const subsequence = "aec";
            const originalString = "abcde";
            const expectedResult = false;
    
            const result:boolean = solution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass subsequence longer than string", () => {
            const subsequence = "aecccccccccc";
            const originalString = "abcde";
            const expectedResult = false;
    
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

    describe("Dynamic programming approach", () => {
        it("should pass test case #1", () => {
            const subsequence = "abc";
            const originalString = "ahbgdc";
            const expectedResult = true;
    
            const result:boolean = dynamicProgrammingSolution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #2", () => {
            const subsequence = "axc";
            const originalString = "ahbgdc";
            const expectedResult = false;
    
            const result:boolean = dynamicProgrammingSolution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #3", () => {
            const subsequence = "ac";
            const originalString = "ahbgdcccccc";
            const expectedResult = true;
    
            const result:boolean = dynamicProgrammingSolution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #4", () => {
            const subsequence = "ace";
            const originalString = "abcde";
            const expectedResult = true;
    
            const result:boolean = dynamicProgrammingSolution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass test case #5", () => {
            const subsequence = "aec";
            const originalString = "abcde";
            const expectedResult = false;
    
            const result:boolean = dynamicProgrammingSolution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass subsequence longer than string", () => {
            const subsequence = "aecccccccccc";
            const originalString = "abcde";
            const expectedResult = false;
    
            const result:boolean = dynamicProgrammingSolution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass same string test case", () => {
            const subsequence = "abc";
            const originalString = "abc";
            const expectedResult = true;
    
            const result:boolean = dynamicProgrammingSolution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass trivial test case", () => {
            const subsequence = "";
            const originalString = "";
            const expectedResult = true;
    
            const result:boolean = dynamicProgrammingSolution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    
        it("should pass low-length test case", () => {
            const subsequence = "a";
            const originalString = "b";
            const expectedResult = false;
    
            const result:boolean = dynamicProgrammingSolution(subsequence, originalString);
            expect(result).to.equal(expectedResult);
        });
    });
});