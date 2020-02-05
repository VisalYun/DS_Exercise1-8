def main():
    string = input("Enter the String: ").split()
    pattern = input("Enter the path: ")
    replace = input("Enter string to replace: ")
    findAndReplace(string, pattern, replace)


def findAndReplace(string, pattern, replace):
    res = ''
    count = 0
    for i in string:
        if pattern == i:
            i = replace
            count += 1
        res = res + i + " "
    checkPatternInString(count, res)


def checkPatternInString(count, res):
    print("Replaced String", res) if count is not 0 else print("No pattern found...")


main()
