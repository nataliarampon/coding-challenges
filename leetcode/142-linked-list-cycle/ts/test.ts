import { expect } from "chai";
import "mocha";
import { generateListWithCycleFromArray, generateNodeListFromArray, ListNode } from "../../util/list/list";
import { detectCycle } from "./solution";

describe("Find Cycle in Linked List",() => {
    it("should return node where cycle begins when cycle is in the middle of the list", () => {
        const input: ListNode | null = generateListWithCycleFromArray([3,2,0,-4], 1);
        const expectedResult = 2;

        const cycleNode: ListNode | null = detectCycle(input);

        expect(cycleNode?.val).to.be.equal(expectedResult);
    });

    it("should return node where cycle begins when cycle is in the beginning of the list", () => {
        const input: ListNode | null = generateListWithCycleFromArray([1,2], 0);
        const expectedResult = 1;

        const cycleNode: ListNode | null = detectCycle(input);

        expect(cycleNode?.val).to.be.equal(expectedResult);
    });

    it("should return head when list has one node and cycle", () => {
        const input: ListNode | null = generateListWithCycleFromArray([4], 0);
        const expectedResult = 4;

        const cycleNode: ListNode | null = detectCycle(input);

        expect(cycleNode?.val).to.be.equal(expectedResult);
    });

    it("should return null when lengthy list has no cycle", () => {
        const input: ListNode | null = generateNodeListFromArray([1,2,3,4]);

        const cycleNode: ListNode | null = detectCycle(input);

        expect(cycleNode).to.be.null;
    });

    it("should return null when list with one node has no cycle", () => {
        const input: ListNode | null = generateNodeListFromArray([1]);

        const cycleNode: ListNode | null = detectCycle(input);

        expect(cycleNode).to.be.null;
    });
});