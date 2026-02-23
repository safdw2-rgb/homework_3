import re
from types import NoneType

contact_book = []

### ------------------- HELPER UTILITIES BLOCK ---------------------- ###

def parse_input(user_input, commands_dict):
    sorted_keys = sorted(commands_dict.keys(), key=len, reverse=True)
    pattern = r'^(' + '|'.join(re.escape(key) for key in sorted_keys) + r')(?:\s|$)'
    match = re.search(pattern, user_input.lower().strip())

    if match:
        command_key = match.group(1)
        args = user_input[match.end():].strip().split()
        return command_key, args

    return None, []


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
    if phone.isdigit():
        return phone

    for number in ban_cymbols:
        phone = phone.strip().replace(number, "")

### ------------------- COMMANDS HANDLER BLOCK ---------------------- ###

@input_error
def add_contact(*args):
    for contact in contact_book:
        if contact["name"] == args[0]:
            return f"Error: Contact {args[0]} is alredy exist."
    checked_number = sanitize_phone_number(args[1])
    if checked_number is None:
        return f"Error: {args[1]} is not a number"
    contact_book.append({"name": args[0], "phone_number": args[1]})
    return f"Contact {args[0]} added."


@input_error
def change_contact(*args):
    if not args[0] in [contact["name"] for contact in contact_book]:
        return f"Contact name: {args[0]} is not exist in contact book."

    if args[1] not in args:
        return "Error: Please provide both name and phone number."
    for contact in contact_book:
        if args[0] == contact["name"]:
           contact["phone_number"] = args[1]
           return f"Contact {args[0]} changed."
        else:
            return f"Error: Contact {args[0]} doesn't exist."


@input_error
def show_phone_number(*args):
    if not args[0] in [contact["name"] for contact in contact_book]:
        return "Contact name is not exist in contact book."
    for contact in contact_book:
        if args[0] == contact["name"]:
            return f"{args[0]}: {contact["phone_number"]}"
        else:
            return f"Error: Contact {args[0]} doesn't exist."


@input_error
def greetings(*args) -> str:
    return "How can I help you?"


@input_error
def show_all(*args) -> str:
    return "\n".join([f"{contact['name']}: {contact['phone_number']}" for contact in contact_book])


@input_error
def exit_command(*args) -> bool:
    print("Good bye!")
    return  False


@input_error
def help_(*args):
    start_part = "This is commands and their description to simplify you usage of CLI-assistant\n"
    commands_and_description = {"hello": "Base start command",
                                "add": "Command for adding new contact in contact book. Requires 2 values: contact name "
                                "and phone number. Should be splited with space",
                                "change": "Command for changing contact in contact book. Requires 2 values: contact name "
                                "and phone number. Should be splited with space",
                                "phone": "Command to show contact phone number. Requires 1 value: contact name",
                                "show all": "Command for showing all contacts and phone numbers from contact book."
    }
    c_n_d_message = "\n".join([f"{command} --- {description}"
                      for command, description in commands_and_description.items()]) + "\n"

    end_part = "If you want to close assistant - use one of the next command: 'exit', 'good bye', 'close'."
    return start_part + c_n_d_message + end_part

### ------------------- MAIN CYCLE ---------------------- ###

def main():
    COMMANDS = {"hello": greetings, "add": add_contact, "change": change_contact,
                "phone": show_phone_number, "show all": show_all, "good bye": exit_command,
                "close": exit_command, "exit": exit_command, "help": help_}
    while True:
        command = input(">>> ")

        parts = command.split()
        if not parts:
            print("Error: Please enter a command.")
            continue

        action_name, args = parse_input(command, COMMANDS)
        action = COMMANDS.get(action_name)
        if isinstance(action, NoneType):
            print("Error: Please enter a correct command or use command 'help' to see valid commands list.")
            continue
        action_result = action(*args)
        if not action_result:
            break
        else:
            print(action_result)


if __name__ == '__main__':
    main()
