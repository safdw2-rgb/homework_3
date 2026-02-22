COMANDS = ["hello", "add", "change", "phone", "show all", "good bye", "close", "exit"]
contact_book = []


def input_error(func):
    def check_errors(*args):
        try:
            return func(*args)
        except IndexError:
            return "Error: Please provide both name and phone number."
        except ValueError:
            return "Error: Please enter correct data."
    return check_errors


@input_error
def add_contact(args):
    contact_book.append({"name": args[0], "phone_number": int(args[1])})
    return f"Contact {args[0]} added."


@input_error
def change_contact(args):
    if args[1] not in args:
        return "Error: Please provide both name and phone number."
    for contact in contact_book:
        if args[0] == contact["name"]:
           contact["phone_number"] = args[1]
           return f"Contact {args[0]} changed."
        else:
            return f"Error: Contact {args[0]} doesn't exist."


@input_error
def show_phone_number(entered_name): 
    for contact in contact_book:
        if entered_name == contact["name"]:
            return f"{entered_name}: {contact["phone_number"]}"
        else:
            return f"Error: Contact {entered_name} doesn't exist."
            


def main():
    while True:
        comand = input(">>> ")

        parts = comand.split()
        if not parts:
            print("Error: Please enter a comand.")
            continue

        if comand in COMANDS[-3:]:
            return "Good Bye!"
        
        action = parts[0].lower()

        if action == COMANDS[0]:
            print("How can I help you?")
        elif action == COMANDS[1]:
            print(add_contact(parts[1:]))
        elif action == COMANDS[2]:
            print(change_contact(parts[1:]))
        elif action == COMANDS[3]:
            print(show_phone_number(parts[1]))
        elif action in COMANDS[4]:
            if len(contact_book) == 0:
                print("Contact book is empty.")
            for i in range(len(contact_book)):
                print(f"{(contact_book[i])["name"]}: {(contact_book[i])["phone_number"]}")
        else:
            print("Error: Please enter a comand.")
            continue
            
        
print(main())