def sortStack(stack):
    stack2 = createStack()
    while not isEmpty(stack):

        tmp = top(stack)
        pop(stack)

        while (isEmpty(stack2) == False and
               int(top(stack2)) > int(tmp)):
            push(stack, top(stack2))
            pop(stack2)

        push(stack2, tmp)

    return stack2


def createStack():
    stack = []
    return stack


def isEmpty(stack1):
    return len(stack1) == 0


def push(stack, item):
    stack.append(item)


def top(stack):
    p = len(stack)
    return stack[p - 1]


def pop(stack):
    if isEmpty(stack):
        print("Stack Underflow ")
        exit(1)

    return stack.pop()


def prints(stack):
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=' ')
    print()


stack = createStack()
arr = [15, 12, 44, 2, 5, 1]
for i in arr:
    push(stack, str(i))

print("Sorted numbers are: ")
sortedStack = sortStack(stack)
prints(sortedStack)
