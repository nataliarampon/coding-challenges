import { ListNode } from "../../util/list/list";


export function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  let remainder = 0;
  let resultHead, result: ListNode | null = null;

  while (l1 || l2) {
    const sum = (l1?.val || 0) + (l2?.val || 0) + remainder;
    if (!resultHead) {
      resultHead = new ListNode(sum % 10);
      result = resultHead;
    } else {
      resultHead.next = new ListNode(sum % 10);
      resultHead = resultHead.next;
    }
    remainder = Math.trunc(sum/10);

    l1 = l1?.next ?? null;
    l2 = l2?.next ?? null;
  }

  if (remainder && resultHead) {
    resultHead.next = new ListNode(remainder);
  }
  
  return result;
}