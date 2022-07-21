import { ListNode } from "../../util/list/list";

export function solution(head: ListNode | null, previous: ListNode | null = null): ListNode | null {
    let current: ListNode | null = null;

    if (head == null) {
        return previous;
    }

    /**
     * This solution is similar to having three pointers. Explaining with the following list as an example: A -> B -> C -> null
     * There's the head pointer, which initially points to A. And each time we're processing things, we need to keep track of
     * the rest of the list to the right, since we override the linking on A. 
     * Thus our current pointer will start pointing to B first thing, to save the rest of the list. So now we have:
     * A (head) -> B (current) -> C -> null     || null (previous)
     */
    current = head.next;
    /**
     * Now, we need to make the current element point to the previous one, to reverse the list.
     * So now we have:
     * A (head) -> null (previous)    ||      B (current) -> C -> null
     * Notice how we'd have lost access to B if we hadn't put it into the current pointer.
     */
    head.next = previous;
    /**
     * The next call will have the following initial setup (notice how the argument previous serves as a third pointer):
     * A (previous) -> null    ||      B (head) -> C -> null
     * This way, in the next call, we will be moving the current pointer to C, and making B point to A, reversing the list.
     */
    return solution(current, head);
}

export function solutionIterative(head: ListNode | null): ListNode | null {
    let previous: ListNode | null = null;
    let current: ListNode | null = null;

    while (head) {
        current = head.next;
        head.next = previous;
        previous = head;
        head = current;
    }
    return previous;
}