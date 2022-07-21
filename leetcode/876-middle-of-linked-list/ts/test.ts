import { expect } from "chai";
import "mocha";
import { compareListNodes, generateNodeListFromArray, ListNode } from "../../util/list/list";
import { middleNode } from "./solution";                            

describe("Middle of Linked List", () => {
    it("should return middle node when list has odd number of nodes", () => {
        const input: ListNode | null = generateNodeListFromArray([1,2,3,4,5]);
        const expectedResult: ListNode | null = generateNodeListFromArray([3,4,5]);

        const result: ListNode | null = middleNode(input);

        expect(compareListNodes(expectedResult, result)).to.be.true;
    });

    it("should return second middle node when list has even number of nodes", () => {
        const input: ListNode | null = generateNodeListFromArray([1,2,3,4,5,6]);
        const expectedResult: ListNode | null = generateNodeListFromArray([4,5,6]);

        const result: ListNode | null = middleNode(input);

        expect(compareListNodes(expectedResult, result)).to.be.true;
    });

    it("should return null when list is empty", () => {
        const input: ListNode | null = generateNodeListFromArray([]);
        const expectedResult: ListNode | null = generateNodeListFromArray([]);

        const result: ListNode | null = middleNode(input);

        expect(compareListNodes(expectedResult, result)).to.be.true;
    });

    it("should return node when list has one node only", () => {
        const input: ListNode | null = generateNodeListFromArray([1]);
        const expectedResult: ListNode | null = generateNodeListFromArray([1]);

        const result: ListNode | null = middleNode(input);

        expect(compareListNodes(expectedResult, result)).to.be.true;
    });
});
