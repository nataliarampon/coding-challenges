import { Set } from "typescript";
import { ListNode } from "../../util/list/list";

export function detectCycle(head: ListNode | null): ListNode | null {
    const visitedNodes: Set<ListNode | void> = new Set();

    while (head) {
        if (visitedNodes.has(head)) {
            return head;
        } else {
            visitedNodes.add(head);
        }
        head = head.next;
    }

    return head;
}