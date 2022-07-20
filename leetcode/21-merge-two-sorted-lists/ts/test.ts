import { expect } from "chai";
import "mocha";
import { compareListNodes, generateNodeListFromArray, ListNode } from "../../util/list/list";
import { solution } from "./solution";

describe("Isomorphic strings", () => {
    it("should pass test case #1", () => {
        const list1: ListNode | null = generateNodeListFromArray([1,2,4]);
        const list2: ListNode | null = generateNodeListFromArray([1,3,4]);
        const expectedResult: ListNode | null = generateNodeListFromArray([1,1,2,3,4,4]);

        const result: ListNode | null = solution(list1, list2);

        expect(compareListNodes(expectedResult, result)).to.be.true;
    });

    it("should pass test case empty list 1", () => {
        const list1: ListNode | null = generateNodeListFromArray([]);
        const list2: ListNode | null = generateNodeListFromArray([0]);
        const expectedResult: ListNode | null = generateNodeListFromArray([0]);

        const result: ListNode | null = solution(list1, list2);

        expect(compareListNodes(expectedResult, result)).to.be.true;
    });

    it("should pass test case empty list 2", () => {
        const list1: ListNode | null = generateNodeListFromArray([0]);
        const list2: ListNode | null = generateNodeListFromArray([]);
        const expectedResult: ListNode | null = generateNodeListFromArray([0]);

        const result: ListNode | null = solution(list1, list2);

        expect(compareListNodes(expectedResult, result)).to.be.true;
    });

    it("should pass test case both empty lists", () => {
        const list1: ListNode | null = generateNodeListFromArray([]);
        const list2: ListNode | null = generateNodeListFromArray([]);
        const expectedResult: ListNode | null = generateNodeListFromArray([]);

        const result: ListNode | null = solution(list1, list2);

        expect(compareListNodes(expectedResult, result)).to.be.true;
    });
});
