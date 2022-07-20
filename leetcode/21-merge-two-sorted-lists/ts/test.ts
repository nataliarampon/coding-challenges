import { expect } from "chai";
import "mocha";
import { ListNode, solution } from "./solution";

describe.only("Isomorphic strings", () => {
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

function generateNodeListFromArray(array:Array<number>): ListNode | null {
    return array.length == 0 ? null : new ListNode(array[0], generateNodeListFromArray(array.slice(1)));
}

function compareListNodes(result: ListNode | null, expectedResult: ListNode | null): boolean {
    let pointerResult: ListNode | null = result;
    let pointerExpected: ListNode | null = expectedResult;
    
    while (pointerExpected && pointerResult) {
        if (pointerExpected.val !== pointerResult.val) {
            return false;
        }
        pointerExpected = pointerExpected.next;
        pointerResult = pointerResult.next;
    } 

    return pointerResult == null && pointerExpected == null;
}
