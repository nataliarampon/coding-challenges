export class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
}

export function generateNodeListFromArray(array:Array<number>): ListNode | null {
    return array.length == 0 ? null : new ListNode(array[0], generateNodeListFromArray(array.slice(1)));
}

export function compareListNodes(result: ListNode | null, expectedResult: ListNode | null): boolean {
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