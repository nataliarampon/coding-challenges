import { ListNode } from "../../util/list/list";

export function solution(input: ListNode | null): ListNode | null {
    if (input != null && input.next != null) {
        const reversed = solution(input.next);
        input.next.next = input;
        input.next = null;
        return reversed;
    }
    return input;
}