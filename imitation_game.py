# On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|'
# •	"Move {number of letters}":
# o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
# o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
# o	Changes all occurrences of the given substring with the replacement text
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by '|' .
# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"


def decode_message(message, operations):
    commands = {
        'Move': lambda x, n: x[n:] + x[:n],
        'Insert': lambda x, i, v: x[:i] + v + x[i:],
        'ChangeAll': lambda x, sub, repl: x.replace(sub, repl)
    }

    result = message

    for operation in operations:
        if operation == "Decode":
            break

        command_parts = operation.split("|")
        command = command_parts[0]

        if command == "Move":
            n = int(command_parts[1])
            result = commands[command](result, n)

        elif command == "Insert":
            index = int(command_parts[1])
            value = command_parts[2]
            result = commands[command](result, index, value)

        elif command == "ChangeAll":
            substring = command_parts[1]
            replacement = command_parts[2]
            result = commands[command](result, substring, replacement)

    return result


# Main execution
encrypted_message = input()
operations = []

while True:
    command = input()
    if command == "Decode":
        operations.append(command)
        break
    operations.append(command)

decrypted_message = decode_message(encrypted_message, operations)
print(f"The decrypted message is: {decrypted_message}")
