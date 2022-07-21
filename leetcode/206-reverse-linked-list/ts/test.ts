import { expect } from "chai";
import "mocha";
import { compareListNodes, generateNodeListFromArray, ListNode } from "../../util/list/list";
import { solution } from "./solution";

describe("Reverse Linked List", () => {
    it("should pass test case #1", () => {
        const input: ListNode | null = generateNodeListFromArray([1,2,3,4,5]);
        const expectedResult: ListNode | null = generateNodeListFromArray([5,4,3,2,1]);

        const revertedList: ListNode | null = solution(input);

        expect(compareListNodes(expectedResult, revertedList)).to.be.true;
    });

    it("should pass test case #2", () => {
        const input: ListNode | null = generateNodeListFromArray([1,2]);
        const expectedResult: ListNode | null = generateNodeListFromArray([2,1]);

        const revertedList: ListNode | null = solution(input);

        expect(compareListNodes(expectedResult, revertedList)).to.be.true;
    });

    it("should pass one node test case", () => {
        const input: ListNode | null = generateNodeListFromArray([1]);
        const expectedResult: ListNode | null = generateNodeListFromArray([1]);

        const revertedList: ListNode | null = solution(input);

        expect(compareListNodes(expectedResult, revertedList)).to.be.true;
    });

    it("should pass empty lists test case", () => {
        const input: ListNode | null = generateNodeListFromArray([]);
        const expectedResult: ListNode | null = generateNodeListFromArray([]);

        const revertedList: ListNode | null = solution(input);

        expect(compareListNodes(expectedResult, revertedList)).to.be.true;
    });
});
