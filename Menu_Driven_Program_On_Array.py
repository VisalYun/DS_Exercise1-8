import array as arr

class Main:
    def Create_Array(self):
        self.a = arr.array('i', map(int, input("Enter the number: ").split()))

    def Display_Array(self):
        print("Array:",self.a)
        print("Suitable heading:",self.a[0])

    def Insert_Array(self, POS, ELEM):
        self.a.insert(POS, ELEM)
        print("After inserted:",self.a)

    def Delete_Array(self, ELEM):
        self.a.pop(ELEM)
        print("After removed",self.a)


print("""  ***Array Menu***
    1. Create Array
    2. Display Array element with suitable heading
    3. Insert Element to Array
    4. Delete Element in Array
    5. Exit
""")
M = Main()
while True:
    select = input("Choose the option: ")
    if select == "1":
        M.Create_Array()
    elif select == "2":
        M.Display_Array()
    elif select == "3":
        M.Insert_Array(int(input("Index Position to insert data: ")), int(input("Insert the data: ")))
    elif select == "4":
        M.Delete_Array(int(input("Index Position to remove the data: ")))
    elif select == "5":
        break


