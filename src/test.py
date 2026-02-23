
contact_book = []


def empty_contact_book():
    if len(contact_book) == 0:
        return "Error: Contact book is empty."


def input_error(func):
    def check_errors(*args):
        try:
            return func(*args)
        except IndexError:
            return "Error: Please provide both name and phone number."
        except ValueError:
            return "Error: Please enter correct data."
    return check_errors


def sanitize_phone_number(phone):
    ban_cymbols = ["+", "(", ")", "-", " "]
    right_phone = phone
    for number in ban_cymbols:
        phone = phone.strip().replace(number, "")
    
    if phone.isdigit():
        return right_phone


@input_error
def add_contact(args):
    for contact in contact_book:
        if contact["name"] == args[0]:
            return f"Error: Contact {args[0]} is alredy exist."
    checked_number = sanitize_phone_number(args[1])
    if checked_number is None: 
        return f"Error: {args[1]} is not a number"
    contact_book.append({"name": args[0], "phone_number": args[1]})
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
        
    return empty_contact_book()

def show_all_numbers():
    if len(contact_book) == 0:
        return "Contact book is empty."
    for i in range(len(contact_book)):
        return f"{(contact_book[i])["name"]}: {(contact_book[i])["phone_number"]}"

@input_error
def show_phone_number(entered_name): 
    for contact in contact_book:
        if entered_name == contact["name"]:
            return f"{entered_name}: {contact["phone_number"]}"
        else:
            return f"Error: Contact {entered_name} doesn't exist."
        
    return empty_contact_book()
            

COMANDS = {
    "hello": "How can I help you?",
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone_number,
    "show all": show_all_numbers,
    "good bye": "Good Bye!",
    "close": "Good Bye!",
    "exit": "Good Bye!"}


def main():
    while True:
        comand = input(">>> ")

        parts = comand.split()
        if not parts:
            print("Error: Please enter a comand.")
            continue

        # action = parts[0].lower()
        # method = COMANDS.get(action)
        
        # if method:
        #     result = method(parts)
        #     if result == "Good Bye!":
        #         return result
        #     print(result)

        # else:
        #     print("Error: Please enter a comand.")
            

print(main())