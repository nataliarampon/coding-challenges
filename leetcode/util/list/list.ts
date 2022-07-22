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

export function generateListWithCycleFromArray(array:Array<number>, cyclePosition: number): ListNode | null {
    let cycleNode: ListNode | null = null;
    let current: ListNode | null;

    if (cyclePosition < 0 || array.length == 0 || (cyclePosition > array.length - 1)) {
        return null;
    }

    const head: ListNode | null = current = new ListNode(array[0], null);

    for (let i = 1; i < array.length; i ++) {
        current.next = new ListNode(array[i], current);
        current = current?.next;
        if (i == cyclePosition) {
            cycleNode = current;
        }
    }

    current.next = cycleNode ?? head;

    return head;
}