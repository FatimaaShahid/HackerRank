PhoneBook = {}
try:
    inp = int(input())
    for i in range(inp):
        text = input().split()
        PhoneBook[text[0]] = text[1]
    
    while True:
        check = input()
        if check in PhoneBook.keys():
            print(check+"="+PhoneBook[check])
        else:
            print("Not found")
except EOFError:
    pass
