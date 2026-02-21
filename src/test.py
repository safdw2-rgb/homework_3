COMANDS = ["hello", "add", "change", "phone", "show all", "good bye", "close", "exit"]
contact_book = []



def leave_program():
    return "Good Bye!"

def main():
    while True:
        comand = input(">>> ")
        parts = comand.split()
        action = parts[0].lower()

        if comand in COMANDS[-3:]:
            return "Good bye"
        elif action = 
        # elif comand == "hello":
        #     print("How can I help you?")
        # elif comand == f"add {name}"

print(main())
