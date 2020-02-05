class Stack:
    def __init__(self, MAX):
        self.MAX = MAX
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        if len(self.items)< self.MAX:
            self.items.append(data)
        else:
            print("# Cannot push: Stack meet maximum size #")
            
    def pop(self):
        return self.items.pop()

    def palindrome(self):
        palindrome = self.items[::-1]
        print("***Palindrome***") if palindrome == self.items else print("****Not Palindrome***")


    def Over_Underflow(self):
        if self.items == []:
            print("Underflow Situation if you try to pop the value")
        elif len(self.items) == self.MAX:
            print("Overflow Condition if you try to push the value")
        else: print("Not in both conditions")

    def display(self):
        print("Stack value:",self.items)


print("""           ***Stack Menu***
    1. Push an element into Stack
    2. Pop an element from Stack
    3. Demonstrate how Stack can be used to check Palindrome
    4. Demonstrate Overflow and Underflow situation on Stack
    5. Display the status of Stack
    6. Exit
    """)
S = Stack(MAX=int(input("Enter the size of the Stack: ")))
while True:
    select = input("^Choose the Menu:^ ")

    if select == "1":
        S.push(int(input("Data to push: ")))

    elif select == "2":
        if S.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', S.pop())

    elif select == "3":
        S.palindrome()

    elif select == "4":
        S.Over_Underflow()

    elif select == "5":
        S.display()

    elif select == "6":
        break
