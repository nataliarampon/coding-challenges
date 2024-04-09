import { expect } from "chai";
import "mocha";
import { compareListNodes, generateNodeListFromArray, ListNode } from "../../util/list/list";
import { addTwoNumbers } from "./solution";

describe.only("Add two numbers in linked lists", () => {
    describe("Iterative solution", () => {
        it("should pass test case #1", () => {
            const firstTerm: ListNode | null = generateNodeListFromArray([2,4,3]);
            const secondTerm: ListNode | null = generateNodeListFromArray([5,6,4]);
            const expectedResult: ListNode | null = generateNodeListFromArray([7,0,8]);
    
            const sum: ListNode | null = addTwoNumbers(firstTerm, secondTerm);

            expect(compareListNodes(expectedResult, sum)).to.be.true;
        });
    
        it("should pass test case #2", () => {
          const firstTerm: ListNode | null = generateNodeListFromArray([2,4,3]);
          const secondTerm: ListNode | null = generateNodeListFromArray([5,6,4]);
          const expectedResult: ListNode | null = generateNodeListFromArray([7,0,8]);

          const sum: ListNode | null = addTwoNumbers(firstTerm, secondTerm);
          
  
          expect(compareListNodes(expectedResult, sum)).to.be.true;
        });
    
        it("should pass one node test case", () => {
          const firstTerm: ListNode | null = generateNodeListFromArray([9]);
          const secondTerm: ListNode | null = generateNodeListFromArray([1]);
          const expectedResult: ListNode | null = generateNodeListFromArray([0,1]);
  
          const sum: ListNode | null = addTwoNumbers(firstTerm, secondTerm);

          expect(compareListNodes(expectedResult, sum)).to.be.true;
        });

        it("should pass empty lists test case", () => {
          const firstTerm: ListNode | null = generateNodeListFromArray([]);
          const secondTerm: ListNode | null = generateNodeListFromArray([]);
          const expectedResult: ListNode | null = generateNodeListFromArray([]);
  
          const sum: ListNode | null = addTwoNumbers(firstTerm, secondTerm);

          expect(compareListNodes(expectedResult, sum)).to.be.true;
        });
    });
    
});
