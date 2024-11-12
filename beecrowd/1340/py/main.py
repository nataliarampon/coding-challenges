def main():
    while True:
        try:
            queue = []
            stack = []
            priority = []
            isQueue = isStack = isPriority = True
            for _ in range(int(input())):
                op, n = map(int, input().split())
                if op == 1:
                    queue.append(n)
                    stack.append(n)
                    priority.append(n)
                else:
                    if n != queue[0]:
                        isQueue = False
                    else:
                        queue.pop(0)

                    if n != stack[-1]:
                        isStack = False
                    else:
                        stack.pop(-1)
            
                    priority.sort()
                    if priority[-1] != n:
                        isPriority = False
                    else:
                        priority.pop(-1)

            if (isStack and isPriority) or (isStack and isQueue) or (isQueue and isPriority):
                print('not sure')
            elif isStack:
                print('stack')
            elif isPriority:
                print('priority queue')
            elif isQueue:
                print('queue')
            else:
                print('impossible')
                    
        except EOFError:
            break

if __name__ == "__main__":
    main()