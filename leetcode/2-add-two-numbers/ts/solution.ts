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

export function addTwoNumbersRecursive(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  return recursiveFunction(0, l1, l2);
}

function recursiveFunction(remainder: number, l1?: ListNode | null, l2?: ListNode | null): ListNode | null {
  if (!l1 && !l2) {
    return remainder != 0 ? new ListNode(remainder) : null;
  }

  const sum = (l1?.val || 0) + (l2?.val || 0) + remainder;
  const result = new ListNode(sum % 10);
  remainder = Math.trunc(sum/10);
  result.next = recursiveFunction(remainder, l1?.next, l2?.next);
  
  return result;
}