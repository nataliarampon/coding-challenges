import { ListNode } from "../../util/list/list";

export function middleNode(head: ListNode | null): ListNode | null {
    let halfPointer: ListNode | null = head;

    while (head != null && head.next != null) {
        halfPointer = halfPointer!.next;
        if (head.next) {
            head = head.next.next;
        }
    }

    return halfPointer;
}